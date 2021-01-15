def get_schedule(year):
    weeks = list(range(1,18))
    schedule_df = pd.DataFrame()
    for w in range(len(weeks)):
        date_string = str(weeks[w]) + '-' + str(year)
        week_scores = Boxscores(weeks[w],year)
        week_games_df = pd.DataFrame()
        for g in range(len(week_scores.games[date_string])):
            game = pd.DataFrame(week_scores.games[date_string][g], index = [0])[['away_name', 'away_abbr','home_name', 'home_abbr','winning_name', 'winning_abbr' ]]
            game['week'] = weeks[w]
            week_games_df = pd.concat([week_games_df,game])
        schedule_df = pd.concat([schedule_df, week_games_df]).reset_index().drop(columns = 'index') 
    return schedule_df