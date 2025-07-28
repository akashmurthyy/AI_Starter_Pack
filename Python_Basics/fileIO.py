from sys import dont_write_bytecode


def read_scores():
    scores_dict = {}
    with open(r"C:\Users\Akash.murthy\PycharmProjects\HelloWorld\sample.txt", "r") as file_object:
        for line in file_object:
            name,score = line.split(',')
            scores_dict[name] = int(score)
    return scores_dict

def get_top_scorer(scores_dict):
    top_name = None
    top_score = float('-inf')
    for name, score in scores_dict.items():
        if score > top_score:
            top_name = name
            top_score = score

    return (top_name, top_score)

def get_average_score(score_dict):
    return sum(score_dict.values()) / len(scores_dict)

scores_dict = read_scores()
top_name,top_score = get_top_scorer(scores_dict)
avg_score = get_average_score(scores_dict)
print(f"Top Scorer: {top_name} with {top_score}")
print(f"Average Score: {avg_score:.2f}")