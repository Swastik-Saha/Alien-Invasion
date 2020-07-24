class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # Read the high score from the high_score.txt file.
        try:
            with open("high_score.txt", 'r') as f_obj:
                high_score = int(f_obj.read())
        except:
            high_score = 0
        self.high_score = high_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
