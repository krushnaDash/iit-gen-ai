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

def llm_function(model,tokenizer,question,option_a,option_b,option_c,option_d):
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

    options = [option_a, option_b, option_c, option_d]
    option_labels = ['A', 'B', 'C', 'D']
    
    # Get token IDs for scoring
    yes_token_id = tokenizer.encode("YES", add_special_tokens=False)[0]
    no_token_id = tokenizer.encode("NO", add_special_tokens=False)[0]
    
    # Create all prompts at once
    prompts = [
        f"Answer the following question by responding YES or NO in upper case only. Nothing else should be in the output.\n\nQuestion: {question}\nProposed Answer: {option}\nIs this the correct answer? "
        for option in options
    ]
    
    # Batch tokenize all prompts
    inputs = tokenizer(prompts, return_tensors="pt", padding=True)
    
    # Create decoder input ids for all prompts in batch
    decoder_input_ids = tokenizer("<pad>", return_tensors="pt", add_special_tokens=False).input_ids
    decoder_input_ids = decoder_input_ids.repeat(4, 1)  # Repeat for batch size of 4
    
    # Single forward pass for all 4 options
    with torch.no_grad():
        outputs = model(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask, decoder_input_ids=decoder_input_ids)
    
    # Get logits for all options at once
    logits = outputs.logits[:, -1, :]  # Shape: [4, vocab_size]
    
    # Calculate scores for all options
    yes_scores = logits[:, yes_token_id]
    no_scores = logits[:, no_token_id]
    scores = yes_scores - no_scores
    
    # Select the option with the highest "Yes" confidence
    best_option_index = scores.argmax().item()
    return option_labels[best_option_index]

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