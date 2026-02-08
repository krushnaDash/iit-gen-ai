"""
Fast test runner: loads model ONCE, then runs all test cases from comprehensive_test.py
in-process. No subprocess overhead — ~30x faster than comprehensive_test.py.
"""
import time
import torch
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration

transformers.logging.set_verbosity_error()
transformers.utils.logging.disable_progress_bar()

# ---- Copy of llm_function from solution.py ----
def llm_function(model, tokenizer, question, option_a, option_b, option_c, option_d):
    options = {"A": option_a, "B": option_b, "C": option_c, "D": option_d}
    opt_keys = list(options.keys())

    true_id = tokenizer("true", add_special_tokens=False).input_ids[0]
    false_id = tokenizer("false", add_special_tokens=False).input_ids[0]
    yes_id = tokenizer("YES", add_special_tokens=False).input_ids[0]
    no_id = tokenizer("NO", add_special_tokens=False).input_ids[0]

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

    yn_prompts = [
        "Answer the following question by responding YES or NO in upper case only. "
        "Nothing else should be in the output.\n\n"
        f"Question: {question}\nProposed Answer: {options[k]}\n"
        "Is this the correct answer? "
        for k in opt_keys
    ]

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
    tf_raw = [float(logits[i, true_id] - logits[i, false_id]) for i in range(4)]
    yn_raw = [float(logits[i + 4, yes_id] - logits[i + 4, no_id]) for i in range(4)]

    tf_t = torch.softmax(torch.tensor(tf_raw), dim=0)
    yn_t = torch.softmax(torch.tensor(yn_raw), dim=0)

    combined = {k: float(tf_t[i] + yn_t[i]) for i, k in enumerate(opt_keys)}

    best = max(combined, key=combined.get)
    final_output = best.strip().upper()
    if final_output not in {"A", "B", "C", "D"}:
        final_output = "A"
    return final_output

# ---- Test cases from comprehensive_test.py ----
test_cases = [
    # === ORIGINAL ASSIGNMENT TESTS ===
    ("Sky color (A)", "What color is the sky on a clear, sunny day?", "Blue", "Green", "Red", "Yellow", "A"),
    ("Sky color (B)", "What color is the sky on a clear, sunny day?", "Green", "Blue", "Red", "Yellow", "B"),
    ("Sky color (C)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Blue", "Yellow", "C"),
    ("Sky color (D)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Yellow", "Blue", "D"),
    # === SCIENCE & NATURE ===
    ("Water formula", "What is the chemical formula for water?", "H2O", "CO2", "NaCl", "O2", "A"),
    ("Speed of light", "What travels at approximately 300,000 km/s?", "Sound", "Light", "Electricity", "Wind", "B"),
    ("DNA shape", "What is the shape of DNA?", "Circle", "Square", "Double helix", "Triangle", "C"),
    ("Photosynthesis output", "What do plants produce during photosynthesis?", "Carbon dioxide", "Nitrogen", "Water", "Oxygen", "D"),
    ("Boiling point water", "At what temperature does water boil at sea level?", "100\u00b0C", "0\u00b0C", "50\u00b0C", "212\u00b0F only", "A"),
    ("Largest planet", "Which is the largest planet in our solar system?", "Saturn", "Jupiter", "Neptune", "Uranus", "B"),
    ("Noble gas", "Which of these is a noble gas?", "Oxygen", "Nitrogen", "Helium", "Hydrogen", "C"),
    ("Red Planet", "Which planet is known as the Red Planet?", "Venus", "Jupiter", "Saturn", "Mars", "D"),
    # === MATHEMATICS ===
    ("2+2", "What is 2 + 2?", "4", "3", "5", "6", "A"),
    ("Square root 144", "What is the square root of 144?", "10", "12", "14", "11", "B"),
    ("Pi value", "What is the approximate value of pi?", "2.14", "4.14", "3.14", "1.14", "C"),
    ("Prime number", "Which of these is a prime number?", "4", "6", "8", "7", "D"),
    ("Pythagorean theorem", "In a right triangle, what does a\u00b2 + b\u00b2 equal?", "c\u00b2", "2c", "c", "ab", "A"),
    ("Fraction to decimal", "What is 1/4 as a decimal?", "0.5", "0.25", "0.75", "0.125", "B"),
    # === GEOGRAPHY ===
    ("Capital France", "What is the capital of France?", "Paris", "London", "Berlin", "Rome", "A"),
    ("Longest river", "What is the longest river in the world?", "Amazon", "Nile", "Mississippi", "Yangtze", "B"),
    ("Largest ocean", "What is the largest ocean on Earth?", "Atlantic", "Indian", "Pacific", "Arctic", "C"),
    ("Mount Everest location", "In which mountain range is Mount Everest located?", "Andes", "Alps", "Rocky Mountains", "Himalayas", "D"),
    ("Country continent", "Which continent is Australia in?", "Australia/Oceania", "Asia", "Europe", "Africa", "A"),
    ("Largest desert", "What is the largest hot desert in the world?", "Gobi", "Sahara", "Arabian", "Kalahari", "B"),
    # === HISTORY ===
    ("First US President", "Who was the first President of the United States?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "A"),
    ("WWII end year", "In what year did World War II end?", "1944", "1945", "1946", "1943", "B"),
    ("Ancient wonder", "The Great Pyramid is located in which country?", "Iraq", "Greece", "Egypt", "Italy", "C"),
    ("Moon landing year", "In what year did humans first land on the Moon?", "1967", "1968", "1970", "1969", "D"),
    # === LITERATURE & ARTS ===
    ("Romeo Juliet author", "Who wrote Romeo and Juliet?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "A"),
    ("Mona Lisa artist", "Who painted the Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Raphael", "Van Gogh", "B"),
    ("1984 author", "Who wrote the novel '1984'?", "Aldous Huxley", "Ray Bradbury", "George Orwell", "H.G. Wells", "C"),
    ("Starry Night artist", "Who painted 'The Starry Night'?", "Monet", "Picasso", "Rembrandt", "Van Gogh", "D"),
    # === BIOLOGY ===
    ("Largest organ", "What is the largest organ in the human body?", "Skin", "Liver", "Heart", "Brain", "A"),
    ("Blood type universal", "Which blood type is known as the universal donor?", "A", "O negative", "B", "AB positive", "B"),
    ("Human chromosomes", "How many chromosomes do humans have?", "23", "44", "46", "48", "C"),
    ("Vitamin D source", "Which vitamin is primarily obtained from sunlight?", "Vitamin A", "Vitamin C", "Vitamin B12", "Vitamin D", "D"),
    # === TECHNOLOGY & COMPUTING ===
    ("Binary base", "What base is the binary number system?", "Base 2", "Base 8", "Base 10", "Base 16", "A"),
    ("WWW inventor", "Who is credited with inventing the World Wide Web?", "Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Mark Zuckerberg", "B"),
    ("RAM meaning", "What does RAM stand for in computing?", "Read Access Memory", "Remote Access Memory", "Random Access Memory", "Run Access Memory", "C"),
    ("First computer", "What was the name of the first electronic general-purpose computer?", "UNIVAC", "IBM PC", "Apple I", "ENIAC", "D"),
    # === LANGUAGE & GRAMMAR ===
    ("Noun definition", "What part of speech names a person, place, or thing?", "Noun", "Verb", "Adjective", "Adverb", "A"),
    ("Plural of child", "What is the plural of 'child'?", "Childs", "Children", "Childes", "Child", "B"),
    ("Opposite of hot", "What is the antonym of 'hot'?", "Warm", "Burning", "Cold", "Tepid", "C"),
    ("Homophone of there", "Which word sounds the same as 'there'?", "Here", "Where", "Hear", "Their", "D"),
    # === TRICKY/EDGE CASES ===
    ("Trick question 1", "How many months have 28 days?", "All 12", "1", "2", "None", "A"),
    ("Common knowledge", "What color is a banana when it's ripe?", "Green", "Yellow", "Red", "Blue", "B"),
    ("Simple logic", "If all cats are animals, and Whiskers is a cat, what is Whiskers?", "A plant", "A mineral", "An animal", "A fungus", "C"),
    ("Basic fact", "How many days are in a week?", "5", "6", "8", "7", "D"),
]

# Shell test cases
shell_test_cases = [
    ("Shell: Sky color (A)", "What color is the sky on a clear, sunny day?", "Blue", "Green", "Red", "Yellow", "A"),
    ("Shell: Sky color (B)", "What color is the sky on a clear, sunny day?", "Green", "Blue", "Red", "Yellow", "B"),
    ("Shell: Sky color (C)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Blue", "Yellow", "C"),
    ("Shell: Sky color (D)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Yellow", "Blue", "D"),
    ("Shell: Sun rises", "Where does the sun rise?", "West", "East", "North", "South", "B"),
    ("Shell: Capital France", "What is the capital of France?", "Paris", "London", "Berlin", "Madrid", "A"),
    ("Shell: Largest planet", "What is the largest planet in our solar system?", "Jupiter", "Saturn", "Earth", "Mars", "A"),
    ("Shell: Water formula", "What is the chemical formula of water?", "CO2", "NaCl", "H2O", "O2", "C"),
    ("Shell: Speed of light", "In which medium does light travel fastest?", "Water", "Vacuum", "Glass", "Air", "B"),
    ("Shell: Programming lang", "Which of the following is a programming language?", "HTML", "CSS", "SQL", "Python", "D"),
    ("Shell: Boiling point", "What is the boiling point of water in Celsius?", "100", "50", "0", "212", "A"),
    ("Shell: Continents", "How many continents are there on Earth?", "5", "6", "7", "8", "C"),
    ("Shell: Largest ocean", "What is the largest ocean on Earth?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "A"),
    ("Shell: DNA full form", "What does DNA stand for?", "Deoxyribose Nucleic Acid", "Deoxyribonucleic Acid", "Dinucleotide Acid", "Dual Nucleic Acid", "B"),
    ("Shell: First US President", "Who was the first President of the United States?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "A"),
    ("Shell: Square root 144", "What is the square root of 144?", "10", "11", "12", "14", "C"),
    ("Shell: Gravity discoverer", "Who is credited with discovering gravity?", "Einstein", "Galileo", "Darwin", "Newton", "D"),
    ("Shell: Capital Japan", "What is the capital of Japan?", "Seoul", "Tokyo", "Beijing", "Bangkok", "B"),
    ("Shell: Photosynthesis gas", "What gas do plants absorb from the atmosphere during photosynthesis?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen", "C"),
    ("Shell: 9x7", "What is 9 multiplied by 7?", "54", "56", "63", "72", "C"),
    ("Shell: FIFO structure", "Which data structure uses First-In-First-Out (FIFO) order?", "Stack", "Queue", "Tree", "Graph", "B"),
    ("Shell: Romeo Juliet", "Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", "B"),
    ("Shell: Red Planet", "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "C"),
    ("Shell: Ripe banana", "What color is a ripe banana?", "Red", "Blue", "Green", "Yellow", "D"),
]

# ---- Categories for breakdown ----
categories = {
    "Original Assignment": (0, 4),
    "Science & Nature": (4, 12),
    "Mathematics": (12, 18),
    "Geography": (18, 24),
    "History": (24, 28),
    "Literature & Arts": (28, 32),
    "Biology": (32, 36),
    "Technology & Computing": (36, 40),
    "Language & Grammar": (40, 44),
    "Tricky/Edge Cases": (44, 48),
}

def run_suite(model, tokenizer, cases, suite_name, cats=None):
    print("=" * 90)
    print(f"  {suite_name}  ({len(cases)} tests)")
    print("=" * 90)

    results = []
    passed = 0
    t0 = time.time()

    for i, (name, q, a, b, c, d, exp) in enumerate(cases, 1):
        start = time.time()
        got = llm_function(model, tokenizer, q, a, b, c, d)
        elapsed = time.time() - start
        ok = got == exp
        if ok:
            passed += 1
        results.append((name, exp, got, ok, elapsed))
        mark = "OK" if ok else "FAIL"
        print(f"  [{i:>2}/{len(cases)}] {mark:>4}  {name:<35} exp={exp} got={got}  ({elapsed:.1f}s)")

    total_time = time.time() - t0

    # Failed tests
    fails = [r for r in results if not r[3]]
    if fails:
        print(f"\n  FAILED TESTS:")
        for name, exp, got, _, _ in fails:
            print(f"    {name:<35} expected={exp}  got={got}")

    # Category breakdown
    if cats:
        print(f"\n  CATEGORY BREAKDOWN:")
        for cat, (s, e) in cats.items():
            cat_res = results[s:e]
            cp = sum(1 for r in cat_res if r[3])
            ct = len(cat_res)
            pct = cp / ct * 100 if ct else 0
            status = "OK" if cp == ct else "!!"
            print(f"    {status} {cat:<30} {cp}/{ct}  ({pct:.0f}%)")

    print(f"\n  RESULT: {passed}/{len(cases)} ({passed/len(cases)*100:.1f}%)  Time: {total_time:.1f}s")
    print("=" * 90)
    return passed, len(cases)


if __name__ == "__main__":
    print("Loading model (once)...")
    load_start = time.time()
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl", local_files_only=True)
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", local_files_only=True)
    torch.manual_seed(42)
    print(f"Model loaded in {time.time() - load_start:.1f}s\n")

    p1, t1 = run_suite(model, tokenizer, test_cases, "COMPREHENSIVE TESTS", categories)
    print()
    p2, t2 = run_suite(model, tokenizer, shell_test_cases, "SHELL TESTS (test_cases.sh)")

    total_p = p1 + p2
    total_t = t1 + t2
    print(f"\n{'='*90}")
    print(f"  COMBINED: {total_p}/{total_t} ({total_p/total_t*100:.1f}%)")
    print(f"  Comprehensive: {p1}/{t1} ({p1/t1*100:.1f}%)  |  Shell: {p2}/{t2} ({p2/t2*100:.1f}%)")
    print(f"{'='*90}")
