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

    options = {"A": option_a, "B": option_b, "C": option_c, "D": option_d}
    opt_keys = list(options.keys())

    # Token IDs for both scoring methods
    true_id = tokenizer("true", add_special_tokens=False).input_ids[0]
    false_id = tokenizer("false", add_special_tokens=False).input_ids[0]
    yes_id = tokenizer("YES", add_special_tokens=False).input_ids[0]
    no_id = tokenizer("NO", add_special_tokens=False).input_ids[0]

    # Method 1: TF-1shot (true/false with 1 few-shot example pair)
    fs = (
        "Question: What language has the most native speakers worldwide?\n"
        "Answer: Mandarin Chinese\n"
        "Is this answer correct? true\n\n"
        "Question: What language has the most native speakers worldwide?\n"
        "Answer: English\n"
        "Is this answer correct? false\n\n"
    )
    tf_prompts = [
        f"{fs}Question: {question}\nAnswer: {options[k]}\n"
        "Is this answer correct?"
        for k in opt_keys
    ]

    # Method 2: S1-style (YES/NO with instruction, zero-shot)
    yn_prompts = [
        "Answer the following question by responding YES or NO in upper case only. "
        "Nothing else should be in the output.\n\n"
        f"Question: {question}\nProposed Answer: {options[k]}\n"
        "Is this the correct answer? "
        for k in opt_keys
    ]

    # Batch all 8 prompts in one forward pass
    all_prompts = tf_prompts + yn_prompts
    inputs = tokenizer(all_prompts, return_tensors="pt", padding=True, truncation=True)
    decoder_input_ids = torch.full((8, 1), tokenizer.pad_token_id, dtype=torch.long)

    with torch.no_grad():
        out = model(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            decoder_input_ids=decoder_input_ids,
        )

    logits = out.logits[:, 0, :]

    # Extract raw scores for each method
    tf_raw = [float(logits[i, true_id] - logits[i, false_id]) for i in range(4)]
    yn_raw = [float(logits[i + 4, yes_id] - logits[i + 4, no_id]) for i in range(4)]

    # Softmax-normalize each method's scores independently
    tf_t = torch.softmax(torch.tensor(tf_raw), dim=0)
    yn_t = torch.softmax(torch.tensor(yn_raw), dim=0)

    # Combine normalized scores
    combined = {k: float(tf_t[i] + yn_t[i]) for i, k in enumerate(opt_keys)}

    best = max(combined, key=combined.get)
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
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl",local_files_only=True)
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl",local_files_only=True)
    ##########################################################################

    """  Call to function that will perform the computation. """
    torch.manual_seed(42)
    out = llm_function(model,tokenizer,question,option_a,option_b,option_c,option_d)
    print(out.strip())

    """ End to call """
