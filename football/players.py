'''Player class to record stats for individual players
'''

class Player:
    '''THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    Generic information about stats for any player on the team 
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals
        self.stats = {'td':touchdowns, 'safety': safety, 'fg': field_goals}  #initializing a dict

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        field_goal_points = 3 * self.stats['fg']
        total_points = td_points + safety_points + field_goal_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

class Defensive_Player(Player):
    def __init__(self, name=None, tackles=5, sacks=4, interceptions=2):
        super().__init__(name)
        self.tackles=tackles
        self.sacks=sacks
        
    def get_defensive_actions(self):
        '''Total times player stopped ofense'''
        total_defenses = self.tackles + self.sacks + self.interceptions

        return total_defenses