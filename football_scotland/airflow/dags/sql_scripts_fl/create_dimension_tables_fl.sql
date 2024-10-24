--CREATE DIMENSION TABLES
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_general_info') THEN
        CREATE TABLE scottish_premiership.dim_general_info (
            game_id SERIAL PRIMARY KEY,
            game_date DATE ,
            fd_time TIME,
            hometeam varchar(255) ,
            awayteam varchar(255),
            fd_fthg varchar(255),
            fd_ftag varchar(255),
            fd_hthg varchar(255),
            fd_htag varchar(255),
            fd_ftr varchar(255),
            fd_htr varchar(255),
            fd_tournament_season varchar(255),
            sofa_tournament_name varchar(255),
            sofa_tournament_country varchar(255),
            sofa_tournament_name_season varchar(255),
            sofa_tournament_season varchar(255),
            sofa_tournament_round varchar(255),
            fbref_time varchar(255),
            fbref_comp varchar(255),
            fbref_round varchar(255),
            fbref_day varchar(255),
            fbref_attendance varchar(255),
            fbref_full_season_format varchar(255),
            fbref_shortened_season varchar(255),
            fbref_match_report_url varchar(255),
            fbref_game_venue_epoch varchar(255),
            fbref_game_venue_time varchar(255),
            fbref_stadium_name varchar(255),
            sofa_city_game_took_place varchar(255),
            sofa_stadium_game_took_place varchar(255),
            german_import_time varchar(255),
            UNIQUE  (game_date,hometeam)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_referees') THEN
        CREATE TABLE scottish_premiership.dim_referees (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_referee varchar(255) ,
            sofa_referee_name varchar(255) ,
            sofa_referee_yellow_cards varchar(255) ,
            sofa_referee_redcards varchar(255) ,
            sofa_referee_yellowredcards varchar(255) ,	
            sofa_referee_games	varchar(255) ,
            sofa_referee_country varchar(255) ,
            fbref_gs_referee varchar(255) ,
            fbref_referee	varchar(255) ,
            fbref_ar_first	varchar(255) ,
            fbref_ar_second	varchar(255) ,
            fbref_fourth_official varchar(255) 
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_managers') THEN
        CREATE TABLE scottish_premiership.dim_managers (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_home_manager_name varchar(255) ,
            sofa_home_manager_slug varchar(255) ,
            sofa_away_manager_name varchar(255) ,
            sofa_away_manager_slug varchar(255) ,
            fbref_hometeam_manager varchar(255) ,	
            fbref_awayteam_manager	varchar(255) 
        );
    END IF;


    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_betting_odds') THEN
        CREATE TABLE scottish_premiership.dim_betting_odds (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_b365h varchar(255) , 
            fd_b365d varchar(255) ,	
            fd_b365a varchar(255) ,	
            fd_bwh varchar(255) ,
            fd_bwd varchar(255) ,	
            fd_bwa varchar(255) 
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_shots') THEN
        CREATE TABLE scottish_premiership.dim_shots (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_hs varchar(255) , 
            fd_as varchar(255) ,	
            fd_hst varchar(255) ,	
            fd_ast varchar(255) ,
            sofa_all_home_total_shots varchar(255) ,	
            sofa_all_away_total_shots varchar(255) ,
            sofa_all_home_shots_on_target varchar(255)  ,
            sofa_all_away_shots_on_target varchar(255) ,
            sofa_all_home_hit_woodwork	varchar(255) ,
            sofa_all_away_hit_woodwork	varchar(255) ,
            sofa_all_home_shots_off_target	varchar(255) ,
            sofa_all_away_shots_off_target	varchar(255) ,
            sofa_all_home_blocked_shots	varchar(255) ,
            sofa_all_away_blocked_shots varchar(255) ,
            sofa_all_home_shots_inside_box varchar(255) ,
            sofa_all_away_shots_inside_box varchar(255) ,
            sofa_all_home_shots_outside_box varchar(255)  ,
            sofa_all_away_shots_outside_box varchar(255) ,
            sofa_first_half_home_total_shots varchar(255) ,
            sofa_first_half_away_total_shots varchar(255) ,
            sofa_first_half_home_shots_on_target varchar(255) ,
            sofa_first_half_away_shots_on_target varchar(255) ,
            sofa_first_half_home_hit_woodwork varchar(255) ,
            sofa_first_half_away_hit_woodwork varchar(255) ,
            sofa_first_half_home_shots_off_target varchar(255) ,
            sofa_first_half_away_shots_off_target varchar(255) ,
            sofa_first_half_home_blocked_shots varchar(255) ,
            sofa_first_half_away_blocked_shots varchar(255) ,
            sofa_first_half_home_shots_inside_box varchar(255) ,
            sofa_first_half_away_shots_inside_box varchar(255) ,
            sofa_first_half_home_shots_outside_box varchar(255) ,
            sofa_first_half_away_shots_outside_box varchar(255) ,
            sofa_second_half_home_total_shots varchar(255) ,
            sofa_second_half_away_total_shots varchar(255) ,
            sofa_second_half_home_shots_on_target varchar(255) ,
            sofa_second_half_away_shots_on_target varchar(255) ,
            sofa_second_half_home_hit_woodwork varchar(255) ,
            sofa_second_half_away_hit_woodwork varchar(255) ,
            sofa_second_half_home_shots_off_target varchar(255) ,
            sofa_second_half_away_shots_off_target varchar(255) ,
            sofa_second_half_home_blocked_shots varchar(255) ,
            sofa_second_half_away_blocked_shots varchar(255) ,
            sofa_second_half_home_shots_inside_box varchar(255) ,
            sofa_second_half_away_shots_inside_box varchar(255) ,
            sofa_second_half_home_shots_outside_box varchar(255) ,
            sofa_second_half_away_shots_outside_box varchar(255) ,
            fbref_hometeam_sh varchar(255) ,
            fbref_hometeam_sot varchar(255) ,
            fbref_hometeam_sot_percentage varchar(255) ,
            fbref_hometeam_gsh varchar(255) ,
            fbref_hometeam_gsot varchar(255) ,
            fbref_hometeam_pk varchar(255) ,
            fbref_hometeam_pkatt varchar(255) ,
            fbref_awayteam_sh varchar(255) ,
            fbref_awayteam_sot varchar(255) ,
            fbref_awayteam_sot_percentage varchar(255) ,
            fbref_awayteam_gsh varchar(255) ,
            fbref_awayteam_gsot varchar(255) ,
            fbref_awayteam_pk varchar(255) ,
            fbref_awayteam_pkatt varchar(255) ,
            fbref_hometeam_shots_on_target_percentage varchar(255) ,
            fbref_awayteam_shots_on_target_percentage varchar(255) ,
            fbref_hometean_shots_not_percentages varchar(255) ,
            fbref_awayteam_shots_not_percentages varchar(255) 
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_fouls') THEN
        CREATE TABLE scottish_premiership.dim_fouls (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_fouls	varchar(255),
            sofa_all_away_fouls varchar(255),
            sofa_all_home_fouled_in_final_third varchar(255),
            sofa_all_away_fouled_in_final_third varchar(255),
            sofa_first_half_home_fouls varchar(255),
            sofa_first_half_away_fouls varchar(255),
            sofa_first_half_home_fouled_in_final_third varchar(255),
            sofa_first_half_away_fouled_in_final_third varchar(255),
            sofa_second_half_home_fouls varchar(255),
            sofa_second_half_away_fouls varchar(255),
            sofa_second_half_home_fouled_in_final_third varchar(255),
            sofa_second_half_away_fouled_in_final_third varchar(255),
            fbref_hometeam_fouls varchar(255),
            fbref_awayteam_fouls varchar(255)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_corners') THEN
        CREATE TABLE scottish_premiership.dim_corners (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_hc varchar(255),
            fd_ac varchar(255),
            sofa_all_home_corner_kicks varchar(255),
            sofa_all_away_corner_kicks varchar(255),
            sofa_first_half_home_corner_kicks varchar(255),
            sofa_first_half_away_corner_kicks varchar(255),
            sofa_second_half_home_corner_kicks varchar(255),
            sofa_second_half_away_corner_kicks varchar(255)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_teams_form') THEN
        CREATE TABLE scottish_premiership.dim_teams_form (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_ftr varchar(255),
            fd_htr varchar(255),
            sofa_hometeam_position varchar(255),
            sofa_hometeam_value varchar(255),
            sofa_hometeam_eam_form varchar(255),
            sofa_awayteam_position varchar(255),
            sofa_awayteam_value varchar(255),
            sofa_awayteam_form varchar(255),
            fbref_hometeam_result varchar(255),
            fbref_awayteam_result varchar(255),
            fbref_hometeam_form varchar(255),
            fbref_awayteam_form varchar(255),
            sofa_hometeam_avgrating varchar(255),
            sofa_awayteam_avgrating varchar(255)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_goalkeeping') THEN
        CREATE TABLE scottish_premiership.dim_goalkeeping (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_goalkeeper_saves varchar(255),
            sofa_all_away_goalkeeper_saves varchar(255),
            sofa_all_home_total_saves varchar(255),
            sofa_all_away_total_saves varchar(255),
            sofa_first_half_home_goalkeeper_saves varchar(255),
            sofa_first_half_away_goalkeeper_saves varchar(255),
            sofa_first_half_home_total_saves varchar(255),
            sofa_first_half_away_total_saves varchar(255),
            sofa_second_half_home_goalkeeper_saves varchar(255),
            sofa_second_half_away_goalkeeper_saves varchar(255),
            sofa_second_half_home_total_saves varchar(255),
            sofa_second_half_away_total_saves varchar(255),
            fbref_hometeam_saves_percentage varchar(255),
            fbref_awayteam_saves_not_percentages varchar(255),
            fbref_hometean_saves_not_percentages varchar(255),
            fbref_awayteam_saves_percentage varchar(255),
            fbref_gs_hometeam_save_percentage varchar(255),
            fbref_gs_awayteam_save_percentage varchar(255)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_passing') THEN
        CREATE TABLE scottish_premiership.dim_passing (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_ball_possession varchar(255),
            sofa_all_away_ball_possession varchar(255),
            sofa_all_home_passes varchar(255),
            sofa_all_away_passes varchar(255),
            sofa_all_home_through_balls varchar(255),
            sofa_all_away_through_balls varchar(255),
            sofa_all_home_accurate_passes varchar(255),
            sofa_all_away_accurate_passes varchar(255),
            sofa_all_home_long_balls varchar(255),
            sofa_all_away_long_balls varchar(255),
            sofa_all_home_crosses varchar(255),
            sofa_all_away_crosses varchar(255),
            sofa_first_half_home_ball_possession varchar(255),	
            sofa_first_half_away_ball_possession varchar(255),
            sofa_first_half_home_passes varchar(255),
            sofa_first_half_away_passes varchar(255),
            sofa_first_half_home_through_balls varchar(255),
            sofa_first_half_away_through_balls varchar(255),
            sofa_first_half_home_accurate_passes varchar(255),
            sofa_first_half_away_accurate_passes varchar(255),
            sofa_first_half_home_long_balls varchar(255),
            sofa_first_half_away_long_balls varchar(255),
            sofa_first_half_home_crosses varchar(255),
            sofa_first_half_away_crosses varchar(255),
            sofa_second_half_home_ball_possession varchar(255),
            sofa_second_half_away_ball_possession varchar(255),
            sofa_second_half_home_passes varchar(255),
            sofa_second_half_away_passes varchar(255),
            sofa_second_half_home_through_balls varchar(255),
            sofa_second_half_away_through_balls varchar(255),
            sofa_second_half_home_accurate_passes varchar(255),
            sofa_second_half_away_accurate_passes varchar(255),
            sofa_second_half_home_long_balls varchar(255) ,
            sofa_second_half_away_long_balls varchar(255),
            sofa_second_half_home_crosses varchar(255),
            sofa_second_half_away_crosses varchar(255) ,
            fbref_score_fixtures_awayteam_poss varchar(255),
            fbref_score_fixtures_hometeam_poss varchar(255),
            fbref_hometeam_crosses varchar(255),
            fbref_awayteam_crosses varchar(255),
            fbref_hometeam_possesion varchar(255) ,
            fbref_awayteam_possesion varchar(255)
        );
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_cards') THEN
        CREATE TABLE scottish_premiership.dim_cards (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fd_hy varchar(255),
            fd_ay varchar(255),
            fd_hr varchar(255),
            fd_ar varchar(255),
            sofa_incident_type_card json,
            sofa_all_home_yellow_cards varchar(255),
            sofa_all_away_yellow_cards varchar(255),
            sofa_first_half_home_yellow_cards varchar(255),
            sofa_first_half_away_yellow_cards varchar(255),
            sofa_second_half_home_yellow_cards varchar(255),
            sofa_second_half_away_yellow_cards varchar(255),
            fbref_yellow_cards_list json,
            fbref_red_cards_list json,
            fbref_yellowred_cards_list json
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_lineups_formations') THEN
        CREATE TABLE scottish_premiership.dim_lineups_formations (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_incident_type_substitution json,
            sofa_home_formation varchar(255),
            sofa_away_formation varchar(255),
            sofa_home_players_list json,
            sofa_away_players_list json,
            sofa_home_starting_eleven json,
            sofa_away_starting_eleven json,
            fbref_score_fixtures_hometeam_captain varchar(255),
            fbref_score_fixtures_awayteam_captain varchar(255),
            fbref_score_fixtures_awayteam_formation varchar(255),
            fbref_score_fixtures_hometeam_formation varchar(255),
            fbref_hometeam_starting_eleven json,
            fbref_hometeam_bench json,
            fbref_hometeam_formation varchar(255),
            fbref_awayteam_starting_eleven json,
            fbref_awayteam_bench json,
            fbref_awayteam_formation varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_chances') THEN
        CREATE TABLE scottish_premiership.dim_chances (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_big_chances varchar(255), 
            sofa_all_away_big_chances varchar(255), 
            sofa_all_home_big_chances_scored varchar(255), 	
            sofa_all_away_big_chances_scored varchar(255), 
            sofa_all_home_big_chances_missed varchar(255), 
            sofa_all_away_big_chances_missed varchar(255), 
            sofa_first_half_home_big_chances varchar(255), 
            sofa_first_half_away_big_chances varchar(255), 
            sofa_first_half_home_big_chances_scored varchar(255), 
            sofa_first_half_away_big_chances_scored varchar(255), 
            sofa_first_half_home_big_chances_missed varchar(255), 
            sofa_first_half_away_big_chances_missed varchar(255), 
            sofa_second_half_home_big_chances varchar(255), 
            sofa_second_half_away_big_chances varchar(255), 
            sofa_second_half_home_big_chances_scored varchar(255), 
            sofa_second_half_away_big_chances_scored varchar(255), 
            sofa_second_half_home_big_chances_missed varchar(255), 
            sofa_second_half_away_big_chances_missed varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_offsides') THEN
        CREATE TABLE scottish_premiership.dim_offsides (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_offsides varchar(255), 
            sofa_all_away_offsides varchar(255), 
            sofa_first_half_home_offsides varchar(255), 
            sofa_first_half_away_offsides varchar(255), 
            sofa_second_half_home_offsides varchar(255), 
            sofa_second_half_away_offsides varchar(255), 
            fbref_hometeam_offsides varchar(255), 
            fbref_awayteam_offsides varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_tackles') THEN
        CREATE TABLE scottish_premiership.dim_tackles (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_tackles	varchar(255), 
            sofa_all_away_tackles varchar(255), 
            sofa_all_home_tackles_won varchar(255), 
            sofa_all_away_tackles_won varchar(255), 
            sofa_all_home_total_tackles varchar(255), 
            sofa_all_away_total_tackles varchar(255), 
            sofa_first_half_home_tackles varchar(255), 
            sofa_first_half_away_tackles varchar(255), 
            sofa_first_half_home_tackles_won varchar(255), 
            sofa_first_half_away_tackles_won varchar(255), 
            sofa_first_half_home_total_tackles varchar(255), 
            sofa_first_half_away_total_tackles varchar(255), 
            sofa_second_half_home_tackles varchar(255), 
            sofa_second_half_away_tackles varchar(255), 
            sofa_second_half_home_tackles_won varchar(255), 
            sofa_second_half_away_tackles_won varchar(255), 
            sofa_second_half_home_total_tackles varchar(255), 
            sofa_second_half_away_total_tackles varchar(255)
          );  
    END IF;


    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_duels') THEN
        CREATE TABLE scottish_premiership.dim_duels (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_duels	varchar(255), 
            sofa_all_away_duels varchar(255) , 
            sofa_all_home_ground_duels varchar(255), 
            sofa_all_away_ground_duels	varchar(255), 
            sofa_all_home_aerial_duels varchar(255), 
            sofa_all_away_aerial_duels varchar(255), 
            sofa_first_half_home_duels varchar(255) , 
            sofa_first_half_away_duels varchar(255) , 
            sofa_first_half_home_ground_duels varchar(255), 
            sofa_first_half_away_ground_duels varchar(255), 
            sofa_first_half_home_aerial_duels varchar(255), 
            sofa_first_half_away_aerial_duels varchar(255), 
            sofa_second_half_home_duels varchar(255), 
            sofa_second_half_away_duels varchar(255), 
            sofa_second_half_home_ground_duels varchar(255), 
            sofa_second_half_away_ground_duels varchar(255) , 
            sofa_second_half_home_aerial_duels varchar(255), 
            sofa_second_half_away_aerial_duels varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_dribbles') THEN
        CREATE TABLE scottish_premiership.dim_dribbles (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_dribbles varchar(255),
            sofa_all_away_dribbles varchar(255),
            sofa_first_half_home_dribbles varchar(255),
            sofa_first_half_away_dribbles varchar(255),
            sofa_second_half_home_dribbles varchar(255),	
            sofa_second_half_away_dribbles varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_clearances') THEN
        CREATE TABLE scottish_premiership.dim_clearances (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_clearances varchar(255),
            sofa_all_away_clearances varchar(255),
            sofa_first_half_home_clearances varchar(255),
            sofa_first_half_away_clearances varchar(255),
            sofa_second_half_home_clearances varchar(255),
            sofa_second_half_away_clearances varchar(255)
          );  
    END IF;


    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_recoveries') THEN
        CREATE TABLE scottish_premiership.dim_recoveries (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_recoveries varchar(255)	,
            sofa_all_away_recoveries varchar(255),
            sofa_first_half_home_recoveries varchar(255),
            sofa_first_half_away_recoveries varchar(255),
            sofa_second_half_home_recoveries varchar(255),
            sofa_second_half_away_recoveries varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_free_kicks') THEN
        CREATE TABLE scottish_premiership.dim_free_kicks (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_free_kicks varchar(255),	
            sofa_all_away_free_kicks varchar(255),
            sofa_first_half_home_free_kicks varchar(255),
            sofa_first_half_away_free_kicks varchar(255),
            sofa_second_half_home_free_kicks varchar(255),
            sofa_second_half_away_free_kicks varchar(255)
          );  
    END IF;


    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_interceptions') THEN
        CREATE TABLE scottish_premiership.dim_interceptions (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_interceptions varchar(255),	
            sofa_all_away_interceptions varchar(255),
            sofa_first_half_home_interceptions varchar(255),
            sofa_first_half_away_interceptions varchar(255),
            sofa_second_half_home_interceptions varchar(255),
            sofa_second_half_away_interceptions varchar(255),
            fbref_hometeam_interceptions varchar(255),
            fbref_awayteam_interceptions varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_goals') THEN
        CREATE TABLE scottish_premiership.dim_goals (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_incident_type_goal json,
            fbref_goal_list json
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_final_third_entries') THEN
        CREATE TABLE scottish_premiership.dim_final_third_entries (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_final_third_entries varchar(255)	,
            sofa_all_away_final_third_entries varchar(255),
            sofa_first_half_home_final_third_entries varchar(255),
            sofa_first_half_away_final_third_entries varchar(255),
            sofa_second_half_home_final_third_entries varchar(255),
            sofa_second_half_away_final_third_entries varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_throw_ins') THEN
        CREATE TABLE scottish_premiership.dim_throw_ins (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_throw_ins varchar(255)	,
            sofa_all_away_throw_ins varchar(255),
            sofa_first_half_home_throw_ins varchar(255),
            sofa_first_half_away_throw_ins varchar(255),
            sofa_second_half_home_throw_ins varchar(255),
            sofa_second_half_away_throw_ins varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_incidents_rest') THEN
        CREATE TABLE scottish_premiership.dim_incidents_rest (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_incident_type_period json,
            sofa_incidents json
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_goal_kicks') THEN
        CREATE TABLE scottish_premiership.dim_goal_kicks (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            sofa_all_home_goal_kicks varchar(255)	,
            sofa_all_away_goal_kicks varchar(255),
            sofa_first_half_home_goal_kicks varchar(255),
            sofa_first_half_away_goal_kicks varchar(255),
            sofa_second_half_home_goal_kicks varchar(255),
            sofa_second_half_away_goal_kicks varchar(255)
          );  
    END IF;

    IF NOT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'scottish_premiership' AND table_name = 'dim_penalties') THEN
        CREATE TABLE scottish_premiership.dim_penalties (
            game_id INT PRIMARY KEY REFERENCES scottish_premiership.dim_general_info (game_id),  
            fbref_hometeam_pkatt varchar(255),
            fbref_hometeam_pka varchar(255),
            fbref_hometeam_pksv varchar(255),
            fbref_hometeam_pkm varchar(255),
            fbref_awayteam_pkatt varchar(255),
            fbref_awayteam_pka varchar(255),
            fbref_awayteam_pksv varchar(255),
            fbref_awayteam_pkm varchar(255),
            fbref_missed_penalty_list json
          );  
    END IF;


END $$;


