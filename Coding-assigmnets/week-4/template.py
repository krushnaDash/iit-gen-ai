"""
This program is build with Flan-T5-XL LLM to be able to determine output of a MCQ question with four options. 

> It accepts five parameters provided as a command line input. 
> The first input represents the question and the next four input are the options. 
> The output should be the option number: A/B/C/D 
> Output should be upper-case
> There should be no additional output including any warning messages in the terminal.
> Remember that your output will be tested against test cases, therefore any deviation from the test cases will be considered incorrect during evaluation.


Syntax: python template.py <string> <string> <string> <string> <string> 

The following example is given for your reference:

 Terminal Input: python template.py "What color is the sky on a clear, sunny day?" "Blue" "Green" "Red" "Yellow"
Terminal Output: A

 Terminal Input: python template.py "What color is the sky on a clear, sunny day?" "Green" "Blue" "Red" "Yellow"
Terminal Output: B

 Terminal Input: python template.py "What color is the sky on a clear, sunny day?" "Green" "Red" "Blue" "Yellow"
Terminal Output: C

 Terminal Input: python template.py "What color is the sky on a clear, sunny day?" "Green" "Red" "Yellow" "Blue"
Terminal Output: D

You are expected to create some examples of your own to test the correctness of your approach.

ALL THE BEST!!
"""

"""
ALERT: * * * No changes are allowed to import statements  * * *
"""
import sys
import torch
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

##### You may comment this section to see verbose -- but you must un-comment this before final submission. ######
transformers.logging.set_verbosity_error()
transformers.utils.logging.disable_progress_bar()
#################################################################################################################

"""
* * * Changes allowed from here  * * * 
"""

def llm_function(model, tokenizer, question, option_a, option_b, option_c, option_d):
    '''
    The steps are given for your reference:

    1. Properly formulate the prompt as per the question - which should output either 'YES' or 'NO'. The output must always be upper-case. You may post-process to get the desired output.
    2. Tokenize the prompt
    3. Pass the tokenized prompt to the model get output in terms of logits since the output is deterministic.  
    4. Extract the correct option from the model.
    5. Clean output and return.
    6. Output is case-sensative: A,B,C or D
    Note: The model (Flan-T5-XL) and tokenizer is already initialized. Do not modify that section.
    '''

    def _batched_seq_nll(prompt_texts, target_texts):

        prompt_inputs = tokenizer(prompt_texts, return_tensors="pt", padding=True, truncation=True)
        label_inputs = tokenizer(target_texts, return_tensors="pt", padding=True, truncation=True)

        labels = label_inputs.input_ids.clone()
        labels[labels == tokenizer.pad_token_id] = -100

        with torch.no_grad():
            out = model(
                input_ids=prompt_inputs.input_ids,
                attention_mask=prompt_inputs.attention_mask,
                labels=labels,
            )

        logits = out.logits
        if logits is None:
            return [float("inf")] * len(prompt_texts)

        vocab_size = logits.shape[-1]
        loss_fct = torch.nn.CrossEntropyLoss(ignore_index=-100, reduction="none")

        token_losses = loss_fct(logits.view(-1, vocab_size), labels.view(-1)).view(labels.size())
        token_mask = (labels != -100).float()
        seq_nll = (token_losses * token_mask).sum(dim=1)
        return [float(x) for x in seq_nll]

    options = {"A": option_a, "B": option_b, "C": option_c, "D": option_d}

    few_shot_examples = (
        "Example 1:\n"
        "Question: What is the capital of France?\n"
        "Proposed Answer: Paris\n"
        "Is this the correct answer? YES\n\n"
        "Example 2:\n"
        "Question: What is the capital of France?\n"
        "Proposed Answer: London\n"
        "Is this the correct answer? NO\n\n"
        "Example 3:\n"
        "Question: What is 9 multiplied by 7?\n"
        "Proposed Answer: 63\n"
        "Is this the correct answer? YES\n\n"
        "Example 4:\n"
        "Question: What is 9 multiplied by 7?\n"
        "Proposed Answer: 56\n"
        "Is this the correct answer? NO\n\n"
    )

    prompts = []
    targets = []
    keys = []
    for k, opt_text in options.items():
        prompt = (
            f"{few_shot_examples}"
            f"Question: {question}\n"
            f"Proposed Answer: {opt_text}\n"
            "Is this the correct answer? Answer YES or NO."
        )
        prompts.append(prompt)
        targets.append("YES")
        keys.append((k, "YES"))

        prompts.append(prompt)
        targets.append("NO")
        keys.append((k, "NO"))

    nlls = _batched_seq_nll(prompts, targets)

    nll_yes = {}
    nll_no = {}
    for (k, yn), nll in zip(keys, nlls):
        if yn == "YES":
            nll_yes[k] = nll
        else:
            nll_no[k] = nll

    scores = {k: (nll_no[k] - nll_yes[k]) for k in options.keys()}

    best = max(scores, key=scores.get)
    final_output = best.strip().upper()
    if final_output not in {"A", "B", "C", "D"}:
        final_output = "A"
    return final_output

"""
ALERT: * * * No changes are allowed below this comment  * * *
"""

if __name__ == '__main__':
    question = sys.argv[1].strip()
    option_a = sys.argv[2].strip()
    option_b = sys.argv[3].strip()
    option_c = sys.argv[4].strip()
    option_d = sys.argv[5].strip()

    ##################### Loading Model and Tokenizer ########################
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl")
    ##########################################################################

    """  Call to function that will perform the computation. """
    torch.manual_seed(42)
    out = llm_function(model,tokenizer,question,option_a,option_b,option_c,option_d)
    print(out.strip())

    """ End to call """