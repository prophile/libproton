
import copy

class ProtonHelper:
    version = "1.0.0"
    def __init__(self, loader):
        self._loader = loader

    def load(self, input_string):
        self._input = self._loader(input_string)
        self._fill_defaults(self._input['teams'])

    @property
    def team_scoresheets(self):
        return copy.deepcopy(self._input['teams'])

    def produce(self, team_scores):
        whole_scores = self.generate_whole_scores(team_scores)
        return {
            "version"      : self.version,
            "match_number" : self._input["match_number"],
            "scores"       : whole_scores,
        }

    def _fill_defaults(self, teams_data):
        for team_data in teams_data.values():
            if "present" not in team_data:
                team_data["present"] = True
            if "disqualified" not in team_data:
                team_data["disqualified"] = False

    def generate_whole_scores(self, team_scores):
        assert self._input is not None, "Cannot generate whole scores without loading input."
        whole = {}
        for tla, team_data in self._input["teams"].items():
            whole[tla] = {
                "zone"          : team_data["zone"],
                "present"       : team_data["present"],
                "disqualified"  : team_data["disqualified"],
                "score"         : team_scores[tla],
            }

        return whole
