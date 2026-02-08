"""Debug: Test MonoT5 logit scoring with different prompt variants on failing tests."""
import torch
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration

transformers.logging.set_verbosity_error()
transformers.utils.logging.disable_progress_bar()

print("Loading model...")
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl", local_files_only=True)
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", local_files_only=True)
torch.manual_seed(42)

true_id = tokenizer("true", add_special_tokens=False).input_ids[0]
false_id = tokenizer("false", add_special_tokens=False).input_ids[0]
yes_id = tokenizer("Yes", add_special_tokens=False).input_ids[0]
no_id = tokenizer("No", add_special_tokens=False).input_ids[0]

def score_options_logit(prompts, tok_pos, tok_neg):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True)
    decoder_input_ids = torch.full((len(prompts), 1), tokenizer.pad_token_id, dtype=torch.long)
    with torch.no_grad():
        out = model(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask, decoder_input_ids=decoder_input_ids)
    logits = out.logits[:, 0, :]
    return [float(logits[i, tok_pos] - logits[i, tok_neg]) for i in range(len(prompts))]

few_shot_6 = (
    "Example 1:\nQuestion: What language has the most native speakers worldwide?\n"
    "Proposed Answer: Mandarin Chinese\nIs the proposed answer correct? true\n\n"
    "Example 2:\nQuestion: What language has the most native speakers worldwide?\n"
    "Proposed Answer: English\nIs the proposed answer correct? false\n\n"
    "Example 3:\nQuestion: What is 15 divided by 3?\n"
    "Proposed Answer: 5\nIs the proposed answer correct? true\n\n"
    "Example 4:\nQuestion: What is 15 divided by 3?\n"
    "Proposed Answer: 4\nIs the proposed answer correct? false\n\n"
    "Example 5:\nQuestion: Which animal is the tallest living terrestrial animal?\n"
    "Proposed Answer: Giraffe\nIs the proposed answer correct? true\n\n"
    "Example 6:\nQuestion: Which animal is the tallest living terrestrial animal?\n"
    "Proposed Answer: Elephant\nIs the proposed answer correct? false\n\n"
)

few_shot_yn = (
    "Example 1:\nQuestion: What language has the most native speakers worldwide?\n"
    "Proposed Answer: Mandarin Chinese\nIs this the correct answer? YES\n\n"
    "Example 2:\nQuestion: What language has the most native speakers worldwide?\n"
    "Proposed Answer: English\nIs this the correct answer? NO\n\n"
    "Example 3:\nQuestion: What is 15 divided by 3?\n"
    "Proposed Answer: 5\nIs this the correct answer? YES\n\n"
    "Example 4:\nQuestion: What is 15 divided by 3?\n"
    "Proposed Answer: 4\nIs this the correct answer? NO\n\n"
    "Example 5:\nQuestion: Which animal is the tallest living terrestrial animal?\n"
    "Proposed Answer: Giraffe\nIs this the correct answer? YES\n\n"
    "Example 6:\nQuestion: Which animal is the tallest living terrestrial animal?\n"
    "Proposed Answer: Elephant\nIs this the correct answer? NO\n\n"
)

# All 24 tests
all_tests = [
    ("Sky color A", "What color is the sky on a clear, sunny day?", ["Blue", "Green", "Red", "Yellow"], "A"),
    ("Sky color B", "What color is the sky on a clear, sunny day?", ["Green", "Blue", "Red", "Yellow"], "B"),
    ("Sky color C", "What color is the sky on a clear, sunny day?", ["Green", "Red", "Blue", "Yellow"], "C"),
    ("Sky color D", "What color is the sky on a clear, sunny day?", ["Green", "Red", "Yellow", "Blue"], "D"),
    ("Sun rise", "Where does the sun rise?", ["West", "East", "North", "South"], "B"),
    ("Capital France", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "A"),
    ("Largest planet", "What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Earth", "Mars"], "A"),
    ("Water formula", "What is the chemical formula of water?", ["CO2", "NaCl", "H2O", "O2"], "C"),
    ("Speed of light", "In which medium does light travel fastest?", ["Water", "Vacuum", "Glass", "Air"], "B"),
    ("Programming lang", "Which of the following is a programming language?", ["HTML", "CSS", "SQL", "Python"], "D"),
    ("Boiling point", "What is the boiling point of water in Celsius?", ["100", "50", "0", "212"], "A"),
    ("Continents", "How many continents are there on Earth?", ["5", "6", "7", "8"], "C"),
    ("Largest ocean", "What is the largest ocean on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "A"),
    ("DNA full form", "What does DNA stand for?", ["Deoxyribose Nucleic Acid", "Deoxyribonucleic Acid", "Dinucleotide Acid", "Dual Nucleic Acid"], "B"),
    ("First President", "Who was the first President of the United States?", ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "A"),
    ("Sqrt 144", "What is the square root of 144?", ["10", "11", "12", "14"], "C"),
    ("Gravity", "Who is credited with discovering gravity?", ["Einstein", "Galileo", "Darwin", "Newton"], "D"),
    ("Capital Japan", "What is the capital of Japan?", ["Seoul", "Tokyo", "Beijing", "Bangkok"], "B"),
    ("Photosynthesis", "What gas do plants absorb from the atmosphere during photosynthesis?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "C"),
    ("9x7", "What is 9 multiplied by 7?", ["54", "56", "63", "72"], "C"),
    ("FIFO", "Which data structure uses First-In-First-Out (FIFO) order?", ["Stack", "Queue", "Tree", "Graph"], "B"),
    ("Romeo Juliet", "Who wrote the play 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "B"),
    ("Red Planet", "Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], "C"),
    ("Banana color", "What color is a ripe banana?", ["Red", "Blue", "Green", "Yellow"], "D"),
]

strategies = {
    "Logit-TF-6shot": {
        "prompt_fn": lambda q, o: f"{few_shot_6}Question: {q}\nProposed Answer: {o}\nIs the proposed answer correct?",
        "pos": true_id, "neg": false_id
    },
    "Logit-TF-0shot": {
        "prompt_fn": lambda q, o: f"Question: {q}\nProposed Answer: {o}\nIs the proposed answer correct?",
        "pos": true_id, "neg": false_id
    },
    "Logit-YN-6shot": {
        "prompt_fn": lambda q, o: f"{few_shot_yn}Question: {q}\nProposed Answer: {o}\nIs this the correct answer?",
        "pos": yes_id, "neg": no_id
    },
    "Logit-TF-MCQ": {
        "prompt_fn": lambda q, o: f"Answer the following question.\n\nQuestion: {q}\nProposed Answer: {o}\nIs the proposed answer correct?",
        "pos": true_id, "neg": false_id
    },
    "Logit-TF-6s-v2": {
        "prompt_fn": lambda q, o: f"{few_shot_6}Question: {q}\nAnswer: {o}\nIs this answer correct?",
        "pos": true_id, "neg": false_id
    },
}

results = {name: [] for name in strategies}

for i, (tname, question, opts, expected) in enumerate(all_tests):
    print(f"[{i+1}/24] {tname}...", end="", flush=True)
    options = {"A": opts[0], "B": opts[1], "C": opts[2], "D": opts[3]}
    for sname, cfg in strategies.items():
        prompts = [cfg["prompt_fn"](question, opt_text) for opt_text in opts]
        scores = score_options_logit(prompts, cfg["pos"], cfg["neg"])
        best_idx = scores.index(max(scores))
        pred = "ABCD"[best_idx]
        results[sname].append((tname, expected, pred))
    print(" done")

print(f"\n{'='*120}")
print("LOGIT STRATEGY COMPARISON")
print(f"{'='*120}")
print(f"{'Test':<22}", end="")
for sname in strategies:
    print(f"{sname:<22}", end="")
print()
print("-" * (22 + 22 * len(strategies)))

for i in range(len(all_tests)):
    tname = all_tests[i][0]
    print(f"{tname:<22}", end="")
    for sname in strategies:
        _, exp, pred = results[sname][i]
        mark = "OK" if pred == exp else f"FAIL({pred})"
        print(f"{mark:<22}", end="")
    print()

print(f"\n{'TOTALS':<22}", end="")
for sname in strategies:
    passed = sum(1 for _, exp, pred in results[sname] if pred == exp)
    print(f"{passed}/24 ({passed/24*100:.0f}%){'':>10}", end="")
print(f"\n{'='*120}")
