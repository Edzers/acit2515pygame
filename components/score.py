import json

class Score:
    def __init__(self):
        self.scores = {}
        self.read_score()

    def write_score(self):
        with open('components/score.json', 'w') as fp:
            json.dump(self.scores, fp)

    def read_score(self):
        with open('components/score.json', 'r') as fp:
            self.scores = json.load(fp)

    def get_score(self):
        return self.scores['new_score']

    def update_score(self, newest_score):
        self.scores['new_score'] = newest_score
        self.scores['high_score']
        if self.scores['new_score'] > self.scores["high_score"]:
            self.scores['high_score'] = newest_score

        self.write_score()

        

    