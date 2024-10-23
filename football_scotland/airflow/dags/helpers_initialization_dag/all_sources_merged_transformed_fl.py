import pandas as pd
from datetime import datetime
import pytz

from .convert_json import safe_json_dumps

def all_sources_merged_transformed_fl():
    #Import the csvs
    only_general_stats = pd.read_csv('/opt/airflow/dags/csvs/first_load_csvs/fbref_only_general_stats_merged_transformed.csv')
    football_data = pd.read_csv('/opt/airflow/dags/csvs/first_load_csvs/football_data_merged_transformed_football_data.csv')
    match_reports = pd.read_csv('/opt/airflow/dags/csvs/first_load_csvs/fbref_match_reports_merged_transformed.csv')
    sofascore = pd.read_csv('/opt/airflow/dags/csvs/first_load_csvs/sofascore_merged_transformed.csv')

    #Renaming dataframes columns for merging
    only_general_stats=only_general_stats.rename(columns={'fbref_only_general_stats_date': 'game_date', 'fbref_only_general_stats_hometeam': 'hometeam'})
    football_data=football_data.rename(columns={'football_data_Date': 'game_date', 'football_data_HomeTeam': 'hometeam'})
    match_reports=match_reports.rename(columns={'fbref_match_reports_game_venue_date': 'game_date', 'fbref_match_reports_hometeam_name': 'hometeam'})
    sofascore=sofascore.rename(columns={'sofascore_game_date': 'game_date', 'sofascore_hometeam_name': 'hometeam'})

    #Merging
    football_data_sofascore = pd.merge(football_data, sofascore, how='left', on=['game_date', 'hometeam'])
    football_data_sofascore_only_general_stats =pd.merge(football_data_sofascore, only_general_stats, how='left', on=['game_date', 'hometeam'])
    football_data_sofascore_only_general_stats_match_reports =pd.merge(football_data_sofascore_only_general_stats, match_reports, how='left', on=['game_date', 'hometeam'])

    # Get the current time in Germany (Europe/Berlin)
    germany_timezone = pytz.timezone('Europe/Berlin')
    current_time_germany = datetime.now(germany_timezone)

    # Add a new column to the DataFrame with the current time
    football_data_sofascore_only_general_stats_match_reports['german_import_time'] = current_time_germany
    """
    new_order =['game_date',
    #time
    'football_data_Time',
    'fbref_match_reports_game_venue_time',
    'fbref_only_general_stats_time',
    #season,countries,general infos
    'football_data_tournament_season',
    'fbref_only_general_stats_comp',
    'fbref_only_general_stats_round',
    'fbref_only_general_stats_day',
    'sofascore_tournament_name',
    'sofascore_tournament_country',
    'sofascore_tournament_name_season',
    'sofascore_tournament_season',
    'sofascore_tournament_round',
    'sofascore_hometeam_country',
    'sofascore_awayteam_country',
    'german_import_time',
    #hometeam_name
    'hometeam',
    #awayteam_name
    'football_data_AwayTeam',
    'fbref_match_reports_awayteam_name',
    'fbref_only_general_stats_awayteam',
    'sofascore_awayteam_name',
    #final_goal_hometeam
    'football_data_FTHG',
    #final_goal_awayteam
    'football_data_FTAG',
    'football_data_FTR',
    'football_data_HTHG',
    'football_data_HTAG',
    'football_data_HTR',
    'football_data_Referee',
    'football_data_HS',
    'football_data_AS',
    'football_data_HST',
    'football_data_AST',
    'football_data_HF',
    'football_data_AF',
    'football_data_HC',
    'football_data_AC',
    'football_data_HY',
    'football_data_AY',
    'football_data_HR',
    'football_data_AR',
    'football_data_B365H',
    'football_data_B365D',
    'football_data_B365A',
    'football_data_BWH',
    'football_data_BWD',
    'football_data_BWA',
    'fbref_match_reports_match_report_url',
    'fbref_match_reports_hometeam_manager',
    'fbref_match_reports_awayteam_manager',
    'fbref_match_reports_hometeam_form',
    'fbref_match_reports_awayteam_form',
    'fbref_match_reports_game_venue_epoch',
    'fbref_match_reports_stadium_name',
    'fbref_match_reports_game_officials',
    'fbref_match_reports_game_attendance',
    'fbref_match_reports_referee',
    'fbref_match_reports_ar1',
    'fbref_match_reports_ar2',
    'fbref_match_reports_fourth_official',
    'fbref_match_reports_hometeam_fouls',
    'fbref_match_reports_awayteam_fouls',
    'fbref_match_reports_hometeam_crosses',
    'fbref_match_reports_awayteam_crosses',
    'fbref_match_reports_hometeam_interceptions',
    'fbref_match_reports_awayteam_interceptions',
    'fbref_match_reports_hometeam_offsides',
    'fbref_match_reports_awayteam_offsides',
    'fbref_match_reports_hometeam_possesion',
    'fbref_match_reports_awayteam_possesion',
    'fbref_match_reports_hometeam_shots_on_target_percentage',
    'fbref_match_reports_awayteam_shots_on_target_percentage',
    'fbref_match_reports_hometean_shots_not_percentages',
    'fbref_match_reports_awayteam_shots_not_percentages',
    'fbref_match_reports_hometeam_saves_percentage',
    'fbref_match_reports_awayteam_saves_not_percentages',
    'fbref_match_reports_hometean_saves_not_percentages',
    'fbref_match_reports_awayteam_saves_percentage',
    'fbref_match_reports_rest_events_list',
    'fbref_match_reports_yellow_cards_list',
    'fbref_match_reports_red_cards_list',
    'fbref_match_reports_goal_list',
    'fbref_match_reports_substitutions_list',
    'fbref_match_reports_missed_penalty_list',
    'fbref_match_reports_hometeam_starting_eleven',
    'fbref_match_reports_hometeam_bench',
    'fbref_match_reports_hometeam_formation',
    'fbref_match_reports_awayteam_starting_eleven',
    'fbref_match_reports_awayteam_bench',
    'fbref_match_reports_awayteam_formation',
    'fbref_only_general_stats_score_fixtures_hometeam_result',
    'fbref_only_general_stats_score_fixtures_hometeam_gf',
    'fbref_only_general_stats_score_fixtures_hometeam_ga',
    'fbref_only_general_stats_score_fixtures_hometeam_poss',
    'fbref_only_general_stats_score_fixtures_hometeam_attendance',
    'fbref_only_general_stats_score_fixtures_hometeam_captain',
    'fbref_only_general_stats_referee',
    'fbref_only_general_stats_score_fixtures_awayteam_result',
    'fbref_only_general_stats_score_fixtures_awayteam_gf',
    'fbref_only_general_stats_score_fixtures_awayteam_ga',
    'fbref_only_general_stats_score_fixtures_awayteam_poss',
    'fbref_only_general_stats_score_fixtures_awayteam_attendance',
    'fbref_only_general_stats_score_fixtures_awayteam_captain',
    'fbref_only_general_stats_score_fixtures_awayteam_formation',
    'fbref_only_general_stats_score_fixtures_hometeam_formation',
    'fbref_only_general_stats_shooting_hometeam_result',
    'fbref_only_general_stats_shooting_hometeam_gf',
    'fbref_only_general_stats_shooting_hometeam_ga',
    'fbref_only_general_stats_shooting_hometeam_gls',
    'fbref_only_general_stats_shooting_hometeam_sh',
    'fbref_only_general_stats_shooting_hometeam_sot',
    'fbref_only_general_stats_shooting_hometeam_sot_percentage',
    'fbref_only_general_stats_shooting_hometeam_gsh',
    'fbref_only_general_stats_shooting_hometeam_gsot',
    'fbref_only_general_stats_shooting_hometeam_pk',
    'fbref_only_general_stats_shooting_hometeam_pkatt',
    'fbref_only_general_stats_shooting_awayteam_result',
    'fbref_only_general_stats_shooting_awayteam_gf',
    'fbref_only_general_stats_shooting_awayteam_ga',
    'fbref_only_general_stats_shooting_awayteam_gls',
    'fbref_only_general_stats_shooting_awayteam_sh',
    'fbref_only_general_stats_shooting_awayteam_sot',
    'fbref_only_general_stats_shooting_awayteam_sot_percentage',
    'fbref_only_general_stats_shooting_awayteam_gsh',
    'fbref_only_general_stats_shooting_awayteam_gsot',
    'fbref_only_general_stats_shooting_awayteam_pk',
    'fbref_only_general_stats_shooting_awayteam_pkatt',
    'fbref_only_general_stats_goalkeeping_hometeam_result',
    'fbref_only_general_stats_goalkeeping_hometeam_gf',
    'fbref_only_general_stats_goalkeeping_hometeam_ga',
    'fbref_only_general_stats_goalkeeping_hometeam_ga.1',
    'fbref_only_general_stats_goalkeeping_hometeam_ga.2',
    'fbref_only_general_stats_goalkeeping_hometeam_ga.3',
    'fbref_only_general_stats_goalkeeping_hometeam_saves',
    'fbref_only_general_stats_goalkeeping_hometeam_save_percentage',
    'fbref_only_general_stats_goalkeeping_hometeam_pkatt',
    'fbref_only_general_stats_goalkeeping_hometeam_pka',
    'fbref_only_general_stats_goalkeeping_hometeam_pksv',
    'fbref_only_general_stats_goalkeeping_hometeam_pkm',
    'fbref_only_general_stats_goalkeeping_awayteam_result',
    'fbref_only_general_stats_goalkeeping_awayteam_gf',
    'fbref_only_general_stats_goalkeeping_awayteam_ga',
    'fbref_only_general_stats_goalkeeping_awayteam_ga.1',
    'fbref_only_general_stats_goalkeeping_awayteam_ga.2',
    'fbref_only_general_stats_goalkeeping_awayteam_ga.3',
    'fbref_only_general_stats_goalkeeping_awayteam_sota',
    'fbref_only_general_stats_goalkeeping_awayteam_saves',
    'fbref_only_general_stats_goalkeeping_awayteam_save_percentage',
    'fbref_only_general_stats_goalkeeping_awayteam_pkatt',
    'fbref_only_general_stats_goalkeeping_awayteam_pka',
    'fbref_only_general_stats_goalkeeping_awayteam_pksv',
    'fbref_only_general_stats_goalkeeping_awayteam_pkm',
    'fbref_only_general_stats_full_season_format',
    'fbref_only_general_stats_shortened_season',
    'sofascore_game_link',
    'sofascore_game_id',
    'sofascore_periods_of_match',
    'sofascore_homescore_ht',
    'sofascore_awayscore_ht',
    'sofascore_homescore_ft',
    'sofascore_awayscore_ft',
    'sofascore_total_goals_ht',
    'sofascore_total_goals_ft',
    'sofascore_home_formation',
    'sofascore_away_formation',
    'sofascore_referee_name',
    'sofascore_referee_yellow_cards',
    'sofascore_referee_redCards',
    'sofascore_referee_yellowRedCards',
    'sofascore_referee_games',
    'sofascore_referee_country',
    'sofascore_all_home_ball_possession',
    'sofascore_all_away_ball_possession',
    'sofascore_all_home_expected_goals',
    'sofascore_all_away_expected_goals',
    'sofascore_all_home_big_chances',
    'sofascore_all_away_big_chances',
    'sofascore_all_home_total_shots',
    'sofascore_all_away_total_shots',
    'sofascore_all_home_goalkeeper_saves',
    'sofascore_all_away_goalkeeper_saves',
    'sofascore_all_home_corner_kicks',
    'sofascore_all_away_corner_kicks',
    'sofascore_all_home_fouls',
    'sofascore_all_away_fouls',
    'sofascore_all_home_passes',
    'sofascore_all_away_passes',
    'sofascore_all_home_tackles',
    'sofascore_all_away_tackles',
    'sofascore_all_home_free_kicks',
    'sofascore_all_away_free_kicks',
    'sofascore_all_home_yellow_cards',
    'sofascore_all_away_yellow_cards',
    'sofascore_all_home_shots_on_target',
    'sofascore_all_away_shots_on_target',
    'sofascore_all_home_hit_woodwork',
    'sofascore_all_away_hit_woodwork',
    'sofascore_all_home_shots_off_target',
    'sofascore_all_away_shots_off_target',
    'sofascore_all_home_blocked_shots',
    'sofascore_all_away_blocked_shots',
    'sofascore_all_home_shots_inside_box',
    'sofascore_all_away_shots_inside_box',
    'sofascore_all_home_shots_outside_box',
    'sofascore_all_away_shots_outside_box',
    'sofascore_all_home_big_chances_scored',
    'sofascore_all_away_big_chances_scored',
    'sofascore_all_home_big_chances_missed',
    'sofascore_all_away_big_chances_missed',
    'sofascore_all_home_through_balls',
    'sofascore_all_away_through_balls',
    'sofascore_all_home_fouled_in_final_third',
    'sofascore_all_away_fouled_in_final_third',
    'sofascore_all_home_offsides',
    'sofascore_all_away_offsides',
    'sofascore_all_home_accurate_passes',
    'sofascore_all_away_accurate_passes',
    'sofascore_all_home_throw_ins',
    'sofascore_all_away_throw_ins',
    'sofascore_all_home_final_third_entries',
    'sofascore_all_away_final_third_entries',
    'sofascore_all_home_long_balls',
    'sofascore_all_away_long_balls',
    'sofascore_all_home_crosses',
    'sofascore_all_away_crosses',
    'sofascore_all_home_duels',
    'sofascore_all_away_duels',
    'sofascore_all_home_dispossessed',
    'sofascore_all_away_dispossessed',
    'sofascore_all_home_ground_duels',
    'sofascore_all_away_ground_duels',
    'sofascore_all_home_aerial_duels',
    'sofascore_all_away_aerial_duels',
    'sofascore_all_home_dribbles',
    'sofascore_all_away_dribbles',
    'sofascore_all_home_tackles_won',
    'sofascore_all_away_tackles_won',
    'sofascore_all_home_total_tackles',
    'sofascore_all_away_total_tackles',
    'sofascore_all_home_interceptions',
    'sofascore_all_away_interceptions',
    'sofascore_all_home_recoveries',
    'sofascore_all_away_recoveries',
    'sofascore_all_home_clearances',
    'sofascore_all_away_clearances',
    'sofascore_all_home_total_saves',
    'sofascore_all_away_total_saves',
    'sofascore_all_home_goals_prevented',
    'sofascore_all_away_goals_prevented',
    'sofascore_all_home_goal_kicks',
    'sofascore_all_away_goal_kicks',
    'sofascore_first_half_home_ball_possession',
    'sofascore_first_half_away_ball_possession',
    'sofascore_first_half_home_expected_goals',
    'sofascore_first_half_away_expected_goals',
    'sofascore_first_half_home_big_chances',
    'sofascore_first_half_away_big_chances',
    'sofascore_first_half_home_total_shots',
    'sofascore_first_half_away_total_shots',
    'sofascore_first_half_home_goalkeeper_saves',
    'sofascore_first_half_away_goalkeeper_saves',
    'sofascore_first_half_home_corner_kicks',
    'sofascore_first_half_away_corner_kicks',
    'sofascore_first_half_home_fouls',
    'sofascore_first_half_away_fouls',
    'sofascore_first_half_home_passes',
    'sofascore_first_half_away_passes',
    'sofascore_first_half_home_tackles',
    'sofascore_first_half_away_tackles',
    'sofascore_first_half_home_free_kicks',
    'sofascore_first_half_away_free_kicks',
    'sofascore_first_half_home_yellow_cards',
    'sofascore_first_half_away_yellow_cards',
    'sofascore_first_half_home_shots_on_target',
    'sofascore_first_half_away_shots_on_target',
    'sofascore_first_half_home_hit_woodwork',
    'sofascore_first_half_away_hit_woodwork',
    'sofascore_first_half_home_shots_off_target',
    'sofascore_first_half_away_shots_off_target',
    'sofascore_first_half_home_blocked_shots',
    'sofascore_first_half_away_blocked_shots',
    'sofascore_first_half_home_shots_inside_box',
    'sofascore_first_half_away_shots_inside_box',
    'sofascore_first_half_home_shots_outside_box',
    'sofascore_first_half_away_shots_outside_box',
    'sofascore_first_half_home_big_chances_scored',
    'sofascore_first_half_away_big_chances_scored',
    'sofascore_first_half_home_big_chances_missed',
    'sofascore_first_half_away_big_chances_missed',
    'sofascore_first_half_home_through_balls',
    'sofascore_first_half_away_through_balls',
    'sofascore_first_half_home_fouled_in_final_third',
    'sofascore_first_half_away_fouled_in_final_third',
    'sofascore_first_half_home_offsides',
    'sofascore_first_half_away_offsides',
    'sofascore_first_half_home_accurate_passes',
    'sofascore_first_half_away_accurate_passes',
    'sofascore_first_half_home_throw_ins',
    'sofascore_first_half_away_throw_ins',
    'sofascore_first_half_home_final_third_entries',
    'sofascore_first_half_away_final_third_entries',
    'sofascore_first_half_home_long_balls',
    'sofascore_first_half_away_long_balls',
    'sofascore_first_half_home_crosses',
    'sofascore_first_half_away_crosses',
    'sofascore_first_half_home_duels',
    'sofascore_first_half_away_duels',
    'sofascore_first_half_home_dispossessed',
    'sofascore_first_half_away_dispossessed',
    'sofascore_first_half_home_ground_duels',
    'sofascore_first_half_away_ground_duels',
    'sofascore_first_half_home_aerial_duels',
    'sofascore_first_half_away_aerial_duels',
    'sofascore_first_half_home_dribbles',
    'sofascore_first_half_away_dribbles',
    'sofascore_first_half_home_tackles_won',
    'sofascore_first_half_away_tackles_won',
    'sofascore_first_half_home_total_tackles',
    'sofascore_first_half_away_total_tackles',
    'sofascore_first_half_home_interceptions',
    'sofascore_first_half_away_interceptions',
    'sofascore_first_half_home_recoveries',
    'sofascore_first_half_away_recoveries',
    'sofascore_first_half_home_clearances',
    'sofascore_first_half_away_clearances',
    'sofascore_first_half_home_total_saves',
    'sofascore_first_half_away_total_saves',
    'sofascore_first_half_home_goals_prevented',
    'sofascore_first_half_away_goals_prevented',
    'sofascore_first_half_home_goal_kicks',
    'sofascore_first_half_away_goal_kicks',
    'sofascore_second_half_home_ball_possession',
    'sofascore_second_half_away_ball_possession',
    'sofascore_second_half_home_expected_goals',
    'sofascore_second_half_away_expected_goals',
    'sofascore_second_half_home_big_chances',
    'sofascore_second_half_away_big_chances',
    'sofascore_second_half_home_total_shots',
    'sofascore_second_half_away_total_shots',
    'sofascore_second_half_home_goalkeeper_saves',
    'sofascore_second_half_away_goalkeeper_saves',
    'sofascore_second_half_home_corner_kicks',
    'sofascore_second_half_away_corner_kicks',
    'sofascore_second_half_home_fouls',
    'sofascore_second_half_away_fouls',
    'sofascore_second_half_home_passes',
    'sofascore_second_half_away_passes',
    'sofascore_second_half_home_tackles',
    'sofascore_second_half_away_tackles',
    'sofascore_second_half_home_free_kicks',
    'sofascore_second_half_away_free_kicks',
    'sofascore_second_half_home_yellow_cards',
    'sofascore_second_half_away_yellow_cards',
    'sofascore_second_half_home_shots_on_target',
    'sofascore_second_half_away_shots_on_target',
    'sofascore_second_half_home_hit_woodwork',
    'sofascore_second_half_away_hit_woodwork',
    'sofascore_second_half_home_shots_off_target',
    'sofascore_second_half_away_shots_off_target',
    'sofascore_second_half_home_blocked_shots',
    'sofascore_second_half_away_blocked_shots',
    'sofascore_second_half_home_shots_inside_box',
    'sofascore_second_half_away_shots_inside_box',
    'sofascore_second_half_home_shots_outside_box',
    'sofascore_second_half_away_shots_outside_box',
    'sofascore_second_half_home_big_chances_scored',
    'sofascore_second_half_away_big_chances_scored',
    'sofascore_second_half_home_big_chances_missed',
    'sofascore_second_half_away_big_chances_missed',
    'sofascore_second_half_home_through_balls',
    'sofascore_second_half_away_through_balls',
    'sofascore_second_half_home_fouled_in_final_third',
    'sofascore_second_half_away_fouled_in_final_third',
    'sofascore_second_half_home_offsides',
    'sofascore_second_half_away_offsides',
    'sofascore_second_half_home_accurate_passes',
    'sofascore_second_half_away_accurate_passes',
    'sofascore_second_half_home_throw_ins',
    'sofascore_second_half_away_throw_ins',
    'sofascore_second_half_home_final_third_entries',
    'sofascore_second_half_away_final_third_entries',
    'sofascore_second_half_home_long_balls',
    'sofascore_second_half_away_long_balls',
    'sofascore_second_half_home_crosses',
    'sofascore_second_half_away_crosses',
    'sofascore_second_half_home_duels',
    'sofascore_second_half_away_duels',
    'sofascore_second_half_home_dispossessed',
    'sofascore_second_half_away_dispossessed',
    'sofascore_second_half_home_ground_duels',
    'sofascore_second_half_away_ground_duels',
    'sofascore_second_half_home_aerial_duels',
    'sofascore_second_half_away_aerial_duels',
    'sofascore_second_half_home_dribbles',
    'sofascore_second_half_away_dribbles',
    'sofascore_second_half_home_tackles_won',
    'sofascore_second_half_away_tackles_won',
    'sofascore_second_half_home_total_tackles',
    'sofascore_second_half_away_total_tackles',
    'sofascore_second_half_home_interceptions',
    'sofascore_second_half_away_interceptions',
    'sofascore_second_half_home_recoveries',
    'sofascore_second_half_away_recoveries',
    'sofascore_second_half_home_clearances',
    'sofascore_second_half_away_clearances',
    'sofascore_second_half_home_total_saves',
    'sofascore_second_half_away_total_saves',
    'sofascore_second_half_home_goals_prevented',
    'sofascore_second_half_away_goals_prevented',
    'sofascore_second_half_home_goal_kicks',
    'sofascore_second_half_away_goal_kicks',
    'sofascore_hometeam_avgRating',
    'sofascore_hometeam_position',
    'sofascore_hometeam_value',
    'sofascore_hometeam_eam_form',
    'sofascore_awayTeam_avgrating',
    'sofascore_awayTeam_position',
    'sofascore_awayTeam_value',
    'sofascore_awayTeam_form',
    'sofascore_match_finished']"""

    # Rearranging the columns
    #football_data_sofascore_only_general_stats_match_reports = football_data_sofascore_only_general_stats_match_reports[new_order]

    #drop columns
    football_data_sofascore_only_general_stats_match_reports= football_data_sofascore_only_general_stats_match_reports.drop(columns=['fbref_only_general_stats_goalkeeping_awayteam_ga.1',
                                                                                                                                     'fbref_only_general_stats_goalkeeping_awayteam_ga.2',
                                                                                                                                     'fbref_only_general_stats_goalkeeping_awayteam_ga.3',
                                                                                                                                     'fbref_only_general_stats_goalkeeping_hometeam_ga.1',
                                                                                                                                     'fbref_only_general_stats_goalkeeping_hometeam_ga.2',
                                                                                                                                     'fbref_only_general_stats_goalkeeping_hometeam_ga.3'])
    
    football_data_sofascore_only_general_stats_match_reports.columns = football_data_sofascore_only_general_stats_match_reports.columns.str.lower()
    # Apply the safe_json_dumps function to the column
    football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_card'] = football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_card'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_goal'] = football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_goal'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_substitution'] = football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_substitution'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_period'] = football_data_sofascore_only_general_stats_match_reports['sofascore_incident_type_period'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_incidents'] = football_data_sofascore_only_general_stats_match_reports['sofascore_incidents'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_home_players_list'] = football_data_sofascore_only_general_stats_match_reports['sofascore_home_players_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_away_players_list'] = football_data_sofascore_only_general_stats_match_reports['sofascore_away_players_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_home_starting_eleven'] = football_data_sofascore_only_general_stats_match_reports['sofascore_home_starting_eleven'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['sofascore_away_starting_eleven'] = football_data_sofascore_only_general_stats_match_reports['sofascore_away_starting_eleven'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_rest_events_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_rest_events_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_yellow_cards_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_yellow_cards_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_red_cards_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_red_cards_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_goal_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_goal_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_substitutions_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_substitutions_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_missed_penalty_list'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_missed_penalty_list'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_hometeam_starting_eleven'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_hometeam_starting_eleven'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_hometeam_bench'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_hometeam_bench'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_awayteam_starting_eleven'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_awayteam_starting_eleven'].apply(safe_json_dumps)
    football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_awayteam_bench'] = football_data_sofascore_only_general_stats_match_reports['fbref_match_reports_awayteam_bench'].apply(safe_json_dumps)

    # Drop duplicates
    # Drop duplicates based on specific columns
    football_data_sofascore_only_general_stats_match_reports = football_data_sofascore_only_general_stats_match_reports.drop_duplicates(subset=['game_date', 'hometeam'])

    football_data_sofascore_only_general_stats_match_reports.to_csv('/opt/airflow/dags/csvs/first_load_csvs/all_sources_merged_transformed.csv', index=False)

if __name__ == "__main__":
    all_sources_merged_transformed_fl()  