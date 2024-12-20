INSERT INTO scottish_premiership.dim_general_info (
    game_date,
    fd_time ,
    hometeam ,
    awayteam ,
    fd_fthg ,
    fd_ftag ,
    fd_hthg ,
    fd_htag ,
    fd_ftr ,
    fd_htr ,
    fd_tournament_season ,
    sofa_tournament_name ,
    sofa_tournament_country ,
    sofa_tournament_name_season ,
    sofa_tournament_season ,
    sofa_tournament_round ,
    fbref_time ,
    fbref_comp ,
    fbref_round ,
    fbref_day ,
    fbref_attendance ,
    fbref_full_season_format ,
    fbref_shortened_season ,
    fbref_match_report_url ,
    fbref_game_venue_epoch ,
    fbref_game_venue_time ,
    fbref_stadium_name ,
    sofa_city_game_took_place,
    sofa_stadium_game_took_place,
    german_import_time 
)
SELECT 
    game_date ,
    football_data_time ,
    hometeam ,
    football_data_awayteam ,
    football_data_fthg ,
    football_data_ftag ,
    football_data_hthg ,
    football_data_htag ,
    football_data_ftr ,
    football_data_htr ,
    football_data_tournament_season ,
    sofascore_tournament_name ,
    sofascore_tournament_country ,
    sofascore_tournament_name_season ,
    sofascore_tournament_season ,
    sofascore_tournament_round ,
    fbref_only_general_stats_time ,
    fbref_only_general_stats_comp ,
    fbref_only_general_stats_round ,
    fbref_only_general_stats_day ,
    fbref_only_general_stats_score_fixtures_hometeam_attendance,
    fbref_only_general_stats_full_season_format ,
    fbref_only_general_stats_shortened_season ,
    fbref_match_reports_match_report_url ,
    fbref_match_reports_game_venue_epoch ,
    fbref_match_reports_game_venue_time ,
    fbref_match_reports_stadium_name ,
    sofascore_city_game_took_place,
    sofascore_stadium_game_took_place,
    german_import_time 
FROM scottish_premiership.staging_table_fl
ORDER BY game_date DESC,football_data_time DESC
ON CONFLICT (game_date, hometeam) DO NOTHING;  -- Prevents duplicate inserts based on game_date and hometeam




--dim referees
INSERT INTO scottish_premiership.dim_referees (
    game_id , 
    fd_referee ,
    sofa_referee_name ,
    sofa_referee_yellow_cards ,
    sofa_referee_redcards ,
    sofa_referee_yellowredcards ,	
    sofa_referee_games	,
    sofa_referee_country ,
    fbref_gs_referee ,--general stats
    fbref_referee	,
    fbref_ar_first	,
    fbref_ar_second	,
    fbref_fourth_official 
)
SELECT 
    dg.game_id, 
    st.football_data_referee, 
    st.sofascore_referee_name, 
    st.sofascore_referee_yellow_cards, 
    st.sofascore_referee_redcards, 
    st.sofascore_referee_yellowredcards, 
    st.sofascore_referee_games, 
    st.sofascore_referee_country, 
    st.fbref_only_general_stats_referee,
    st.fbref_match_reports_referee,
    st.fbref_match_reports_ar1,
    st.fbref_match_reports_ar2,
    st.fbref_match_reports_fourth_official   
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;  -- Prevents inserting duplicate statistics for the same game_id


--dim_managers
INSERT INTO scottish_premiership.dim_managers (
    game_id, 
    sofa_home_manager_name, 
    sofa_home_manager_slug,	
    sofa_away_manager_name,	
    sofa_away_manager_slug,
    fbref_hometeam_manager,	
    fbref_awayteam_manager
)
SELECT 
    dg.game_id, 
    st.sofascore_home_manager_name, 
    st.sofascore_home_manager_slug,	
    st.sofascore_away_manager_name,	
    st.sofascore_away_manager_slug,
    st.fbref_match_reports_hometeam_manager,	
    st.fbref_match_reports_awayteam_manager
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


--dim_betting_odds
INSERT INTO scottish_premiership.dim_betting_odds (
    game_id, 
    fd_b365h, 
    fd_b365d,	
    fd_b365a,	
    fd_bwh,
    fd_bwd,	
    fd_bwa
)
SELECT 
    dg.game_id, 
    st.football_data_b365h, 
    st.football_data_b365d,	
    st.football_data_b365a,	
    st.football_data_bwh,
    st.football_data_bwd,	
    st.football_data_bwa
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


--dim_shots
INSERT INTO scottish_premiership.dim_shots (
    game_id, 
    fd_hs, 
    fd_as,	
    fd_hst,	
    fd_ast,
    sofa_all_home_total_shots,	
    sofa_all_away_total_shots,
    sofa_all_home_shots_on_target,
    sofa_all_away_shots_on_target,
    sofa_all_home_hit_woodwork	,
    sofa_all_away_hit_woodwork	,
    sofa_all_home_shots_off_target	,
    sofa_all_away_shots_off_target	,
    sofa_all_home_blocked_shots	,
    sofa_all_away_blocked_shots,
    sofa_all_home_shots_inside_box,
    sofa_all_away_shots_inside_box,
    sofa_all_home_shots_outside_box,
    sofa_all_away_shots_outside_box,
    sofa_first_half_home_total_shots,
    sofa_first_half_away_total_shots,
    sofa_first_half_home_shots_on_target,
    sofa_first_half_away_shots_on_target,
    sofa_first_half_home_hit_woodwork,
    sofa_first_half_away_hit_woodwork,
    sofa_first_half_home_shots_off_target,
    sofa_first_half_away_shots_off_target,
    sofa_first_half_home_blocked_shots,
    sofa_first_half_away_blocked_shots,
    sofa_first_half_home_shots_inside_box,
    sofa_first_half_away_shots_inside_box,
    sofa_first_half_home_shots_outside_box,
    sofa_first_half_away_shots_outside_box,
    sofa_second_half_home_total_shots,
    sofa_second_half_away_total_shots,
    sofa_second_half_home_shots_on_target,
    sofa_second_half_away_shots_on_target,
    sofa_second_half_home_hit_woodwork,
    sofa_second_half_away_hit_woodwork,
    sofa_second_half_home_shots_off_target,
    sofa_second_half_away_shots_off_target,
    sofa_second_half_home_blocked_shots,
    sofa_second_half_away_blocked_shots,
    sofa_second_half_home_shots_inside_box,
    sofa_second_half_away_shots_inside_box,
    sofa_second_half_home_shots_outside_box,
    sofa_second_half_away_shots_outside_box,
    fbref_hometeam_sh,
    fbref_hometeam_sot,
    fbref_hometeam_sot_percentage,
    fbref_hometeam_gsh,
    fbref_hometeam_gsot,
    fbref_hometeam_pk,
    fbref_hometeam_pkatt,
    fbref_awayteam_sh,
    fbref_awayteam_sot,
    fbref_awayteam_sot_percentage,
    fbref_awayteam_gsh,
    fbref_awayteam_gsot,
    fbref_awayteam_pk,
    fbref_awayteam_pkatt,
    fbref_hometeam_shots_on_target_percentage,
    fbref_awayteam_shots_on_target_percentage,
    fbref_hometean_shots_not_percentages,
    fbref_awayteam_shots_not_percentages
)
SELECT 
    dg.game_id, 
    st.football_data_hs, 
    st.football_data_as,	
    st.football_data_hst,	
    st.football_data_ast,
    st.sofascore_all_home_total_shots,	
    st.sofascore_all_away_total_shots,
    st.sofascore_all_home_shots_on_target,
    st.sofascore_all_away_shots_on_target,
    st.sofascore_all_home_hit_woodwork	,
    st.sofascore_all_away_hit_woodwork	,
    st.sofascore_all_home_shots_off_target,	
    st.sofascore_all_away_shots_off_target,	
    st.sofascore_all_home_blocked_shots	,
    st.sofascore_all_away_blocked_shots,
    st.sofascore_all_home_shots_inside_box,
    st.sofascore_all_away_shots_inside_box,
    st.sofascore_all_home_shots_outside_box,
    st.sofascore_all_away_shots_outside_box,
    st.sofascore_first_half_home_total_shots,
    st.sofascore_first_half_away_total_shots,
    st.sofascore_first_half_home_shots_on_target,
    st.sofascore_first_half_away_shots_on_target,
    st.sofascore_first_half_home_hit_woodwork,
    st.sofascore_first_half_away_hit_woodwork,
    st.sofascore_first_half_home_shots_off_target,
    st.sofascore_first_half_away_shots_off_target,
    st.sofascore_first_half_home_blocked_shots,
    st.sofascore_first_half_away_blocked_shots,
    st.sofascore_first_half_home_shots_inside_box,
    st.sofascore_first_half_away_shots_inside_box,
    st.sofascore_first_half_home_shots_outside_box,
    st.sofascore_first_half_away_shots_outside_box,
    st.sofascore_second_half_home_total_shots,
    st.sofascore_second_half_away_total_shots,
    st.sofascore_second_half_home_shots_on_target,
    st.sofascore_second_half_away_shots_on_target,
    st.sofascore_second_half_home_hit_woodwork,
    st.sofascore_second_half_away_hit_woodwork,
    st.sofascore_second_half_home_shots_off_target,
    st.sofascore_second_half_away_shots_off_target,
    st.sofascore_second_half_home_blocked_shots,
    st.sofascore_second_half_away_blocked_shots,
    st.sofascore_second_half_home_shots_inside_box,
    st.sofascore_second_half_away_shots_inside_box,
    st.sofascore_second_half_home_shots_outside_box,
    st.sofascore_second_half_away_shots_outside_box,
    st.fbref_only_general_stats_shooting_hometeam_sh,
    st.fbref_only_general_stats_shooting_hometeam_sot,
    st.fbref_only_general_stats_shooting_hometeam_sot_percentage,
    st.fbref_only_general_stats_shooting_hometeam_gsh,
    st.fbref_only_general_stats_shooting_hometeam_gsot,
    st.fbref_only_general_stats_shooting_hometeam_pk,
    st.fbref_only_general_stats_shooting_hometeam_pkatt,
    st.fbref_only_general_stats_shooting_awayteam_sh,
    st.fbref_only_general_stats_shooting_awayteam_sot,
    st.fbref_only_general_stats_shooting_awayteam_sot_percentage,
    st.fbref_only_general_stats_shooting_awayteam_gsh,
    st.fbref_only_general_stats_shooting_awayteam_gsot,
    st.fbref_only_general_stats_shooting_awayteam_pk,
    st.fbref_only_general_stats_shooting_awayteam_pkatt,
    st.fbref_match_reports_hometeam_shots_on_target_percentage,
    st.fbref_match_reports_awayteam_shots_on_target_percentage,
    st.fbref_match_reports_hometean_shots_not_percentages,
    st.fbref_match_reports_awayteam_shots_not_percentages
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;



--dim_fouls
INSERT INTO scottish_premiership.dim_fouls (
    game_id, 
    sofa_all_home_fouls	,
    sofa_all_away_fouls,
    sofa_all_home_fouled_in_final_third,
    sofa_all_away_fouled_in_final_third,
    sofa_first_half_home_fouls,
    sofa_first_half_away_fouls,
    sofa_first_half_home_fouled_in_final_third,
    sofa_first_half_away_fouled_in_final_third,
    sofa_second_half_home_fouls,
    sofa_second_half_away_fouls,
    sofa_second_half_home_fouled_in_final_third,
    sofa_second_half_away_fouled_in_final_third,
    fbref_hometeam_fouls,
    fbref_awayteam_fouls
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_fouls	,
    st.sofascore_all_away_fouls ,
    st.sofascore_all_home_fouled_in_final_third ,
    st.sofascore_all_away_fouled_in_final_third ,
    st.sofascore_first_half_home_fouls ,
    st.sofascore_first_half_away_fouls ,
    st.sofascore_first_half_home_fouled_in_final_third ,
    st.sofascore_first_half_away_fouled_in_final_third ,
    st.sofascore_second_half_home_fouls ,
    st.sofascore_second_half_away_fouls ,
    st.sofascore_second_half_home_fouled_in_final_third ,
    st.sofascore_second_half_away_fouled_in_final_third ,
    st.fbref_match_reports_hometeam_fouls ,
    st.fbref_match_reports_awayteam_fouls
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_corners
INSERT INTO scottish_premiership.dim_corners (
    game_id, 
    fd_hc,
    fd_ac,
    sofa_all_home_corner_kicks,
    sofa_all_away_corner_kicks,
    sofa_first_half_home_corner_kicks,
    sofa_first_half_away_corner_kicks,
    sofa_second_half_home_corner_kicks,
    sofa_second_half_away_corner_kicks
)
SELECT 
    dg.game_id, 
    st.football_data_hc,
    st.football_data_ac,
    st.sofascore_all_home_corner_kicks,
    st.sofascore_all_away_corner_kicks,
    st.sofascore_first_half_home_corner_kicks,
    st.sofascore_first_half_away_corner_kicks,
    st.sofascore_second_half_home_corner_kicks,
    st.sofascore_second_half_away_corner_kicks
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim teams_form
INSERT INTO scottish_premiership.dim_teams_form (
    game_id, 
    fd_ftr,
    fd_htr,
    sofa_hometeam_position,
    sofa_hometeam_value,
    sofa_hometeam_eam_form,
    sofa_awayteam_position,
    sofa_awayteam_value,
    sofa_awayteam_form,
    fbref_hometeam_result,
    fbref_awayteam_result,
    fbref_hometeam_form,
    fbref_awayteam_form,
    sofa_hometeam_avgrating,
    sofa_awayteam_avgrating
)
SELECT 
    dg.game_id, 
    st.football_data_ftr,
    st.football_data_htr,
    st.sofascore_hometeam_position,
    st.sofascore_hometeam_value,
    st.sofascore_hometeam_eam_form,
    st.sofascore_awayteam_position,
    st.sofascore_awayteam_value,
    st.sofascore_awayteam_form,
    st.fbref_only_general_stats_score_fixtures_hometeam_result,
    st.fbref_only_general_stats_score_fixtures_awayteam_result,
    st.fbref_match_reports_hometeam_form,
    st.fbref_match_reports_awayteam_form,
    st.sofascore_hometeam_avgrating,
    st.sofascore_awayteam_avgrating
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


	


--dim goalkeeping
INSERT INTO scottish_premiership.dim_goalkeeping (
    game_id, 
    sofa_all_home_goalkeeper_saves,
    sofa_all_away_goalkeeper_saves,
    sofa_all_home_total_saves,
    sofa_all_away_total_saves,
    sofa_first_half_home_goalkeeper_saves,
    sofa_first_half_away_goalkeeper_saves,
    sofa_first_half_home_total_saves,
    sofa_first_half_away_total_saves,
    sofa_second_half_home_goalkeeper_saves,
    sofa_second_half_away_goalkeeper_saves,
    sofa_second_half_home_total_saves,
    sofa_second_half_away_total_saves,
    fbref_hometeam_saves_percentage,
    fbref_awayteam_saves_not_percentages,
    fbref_hometean_saves_not_percentages,
    fbref_awayteam_saves_percentage,
    fbref_gs_hometeam_save_percentage,
    fbref_gs_awayteam_save_percentage
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_goalkeeper_saves,
    st.sofascore_all_away_goalkeeper_saves,
    st.sofascore_all_home_total_saves,
    st.sofascore_all_away_total_saves,
    st.sofascore_first_half_home_goalkeeper_saves,
    st.sofascore_first_half_away_goalkeeper_saves,
    st.sofascore_first_half_home_total_saves,
    st.sofascore_first_half_away_total_saves,
    st.sofascore_second_half_home_goalkeeper_saves,
    st.sofascore_second_half_away_goalkeeper_saves,
    st.sofascore_second_half_home_total_saves,
    st.sofascore_second_half_away_total_saves,
    st.fbref_match_reports_hometeam_saves_percentage,
    st.fbref_match_reports_awayteam_saves_not_percentages,
    st.fbref_match_reports_hometean_saves_not_percentages,
    st.fbref_match_reports_awayteam_saves_percentage,
    st.fbref_only_general_stats_goalkeeping_hometeam_save_percentage,
    st.fbref_only_general_stats_goalkeeping_awayteam_save_percentage
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

 
--dim_passing
INSERT INTO scottish_premiership.dim_passing (
    game_id, 
    sofa_all_home_ball_possession,
    sofa_all_away_ball_possession,
    sofa_all_home_passes,
    sofa_all_away_passes,
    sofa_all_home_through_balls,
    sofa_all_away_through_balls,
    sofa_all_home_accurate_passes,
    sofa_all_away_accurate_passes,
    sofa_all_home_long_balls,
    sofa_all_away_long_balls,
    sofa_all_home_crosses,
    sofa_all_away_crosses,
    sofa_first_half_home_ball_possession,	
    sofa_first_half_away_ball_possession,
    sofa_first_half_home_passes,
    sofa_first_half_away_passes,
    sofa_first_half_home_through_balls,
    sofa_first_half_away_through_balls,
    sofa_first_half_home_accurate_passes,
    sofa_first_half_away_accurate_passes,
    sofa_first_half_home_long_balls,
    sofa_first_half_away_long_balls,
    sofa_first_half_home_crosses,
    sofa_first_half_away_crosses,
    sofa_second_half_home_ball_possession,
    sofa_second_half_away_ball_possession,
    sofa_second_half_home_passes,
    sofa_second_half_away_passes,
    sofa_second_half_home_through_balls,
    sofa_second_half_away_through_balls,
    sofa_second_half_home_accurate_passes,
    sofa_second_half_away_accurate_passes,
    sofa_second_half_home_long_balls,
    sofa_second_half_away_long_balls,
    sofa_second_half_home_crosses,
    sofa_second_half_away_crosses,
    fbref_score_fixtures_awayteam_poss,
    fbref_score_fixtures_hometeam_poss,
    fbref_hometeam_crosses,
    fbref_awayteam_crosses,
    fbref_hometeam_possesion,
    fbref_awayteam_possesion
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_ball_possession, 	
    st.sofascore_all_away_ball_possession, 
    st.sofascore_all_home_passes, 
    st.sofascore_all_away_passes, 
    st.sofascore_all_home_through_balls, 
    st.sofascore_all_away_through_balls, 
    st.sofascore_all_home_accurate_passes, 
    st.sofascore_all_away_accurate_passes, 
    st.sofascore_all_home_long_balls, 
    st.sofascore_all_away_long_balls, 
    st.sofascore_all_home_crosses, 
    st.sofascore_all_away_crosses, 
    st.sofascore_first_half_home_ball_possession, 	
    st.sofascore_first_half_away_ball_possession, 
    st.sofascore_first_half_home_passes, 
    st.sofascore_first_half_away_passes, 
    st.sofascore_first_half_home_through_balls, 
    st.sofascore_first_half_away_through_balls, 
    st.sofascore_first_half_home_accurate_passes, 
    st.sofascore_first_half_away_accurate_passes, 
    st.sofascore_first_half_home_long_balls, 
    st.sofascore_first_half_away_long_balls, 
    st.sofascore_first_half_home_crosses, 
    st.sofascore_first_half_away_crosses, 
    st.sofascore_second_half_home_ball_possession, 
    st.sofascore_second_half_away_ball_possession, 
    st.sofascore_second_half_home_passes, 
    st.sofascore_second_half_away_passes, 
    st.sofascore_second_half_home_through_balls, 
    st.sofascore_second_half_away_through_balls, 
    st.sofascore_second_half_home_accurate_passes, 
    st.sofascore_second_half_away_accurate_passes, 
    st.sofascore_second_half_home_long_balls, 
    st.sofascore_second_half_away_long_balls, 
    st.sofascore_second_half_home_crosses, 
    st.sofascore_second_half_away_crosses, 
    st.fbref_only_general_stats_score_fixtures_awayteam_poss, 
    st.fbref_only_general_stats_score_fixtures_hometeam_poss, 
    st.fbref_match_reports_hometeam_crosses, 
    st.fbref_match_reports_awayteam_crosses, 
    st.fbref_match_reports_hometeam_possesion, 
    st.fbref_match_reports_awayteam_possesion
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_cards
INSERT INTO scottish_premiership.dim_cards (
    game_id, 
    fd_hy,
    fd_ay,
    fd_hr,
    fd_ar,
    sofa_incident_type_card,
    sofa_all_home_yellow_cards,
    sofa_all_away_yellow_cards,
    sofa_first_half_home_yellow_cards,
    sofa_first_half_away_yellow_cards,
    sofa_second_half_home_yellow_cards,
    sofa_second_half_away_yellow_cards,
    fbref_yellow_cards_list,
    fbref_red_cards_list,
    fbref_yellowred_cards_list
)
SELECT 
    dg.game_id, 
    st.football_data_hy,
    st.football_data_ay,
    st.football_data_hr,
    st.football_data_ar,
    st.sofascore_incident_type_card,
    st.sofascore_all_home_yellow_cards,
    st.sofascore_all_away_yellow_cards,
    st.sofascore_first_half_home_yellow_cards,
    st.sofascore_first_half_away_yellow_cards,
    st.sofascore_second_half_home_yellow_cards,
    st.sofascore_second_half_away_yellow_cards,
    st.fbref_match_reports_yellow_cards_list,
    st.fbref_match_reports_red_cards_list,
    st.fbref_match_reports_rest_events_list
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;




--dim_lineups_formations
INSERT INTO scottish_premiership.dim_lineups_formations (
    game_id, 
    sofa_incident_type_substitution,
    sofa_home_formation,
    sofa_away_formation,
    sofa_home_players_list,
    sofa_away_players_list,
    sofa_home_starting_eleven,
    sofa_away_starting_eleven,
    fbref_score_fixtures_hometeam_captain,
    fbref_score_fixtures_awayteam_captain,
    fbref_score_fixtures_awayteam_formation,
    fbref_score_fixtures_hometeam_formation,
    fbref_hometeam_starting_eleven,
    fbref_hometeam_bench,
    fbref_hometeam_formation,
    fbref_awayteam_starting_eleven,
    fbref_awayteam_bench,
    fbref_awayteam_formation
)
SELECT 
    dg.game_id, 
    st.sofascore_incident_type_substitution,
    st.sofascore_home_formation,
    st.sofascore_away_formation,
    st.sofascore_home_players_list,
    st.sofascore_away_players_list,
    st.sofascore_home_starting_eleven,
    st.sofascore_away_starting_eleven,
    st.fbref_only_general_stats_score_fixtures_hometeam_captain,
    st.fbref_only_general_stats_score_fixtures_awayteam_captain,
    st.fbref_only_general_stats_score_fixtures_awayteam_formation,
    st.fbref_only_general_stats_score_fixtures_hometeam_formation,
    st.fbref_match_reports_hometeam_starting_eleven,
    st.fbref_match_reports_hometeam_bench,
    st.fbref_match_reports_hometeam_formation,
    st.fbref_match_reports_awayteam_starting_eleven,
    st.fbref_match_reports_awayteam_bench,
    st.fbref_match_reports_awayteam_formation
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


-- dim_chances
INSERT INTO scottish_premiership.dim_chances (
    game_id, 
    sofa_all_home_big_chances, 
    sofa_all_away_big_chances, 
    sofa_all_home_big_chances_scored, 	
    sofa_all_away_big_chances_scored, 
    sofa_all_home_big_chances_missed, 
    sofa_all_away_big_chances_missed, 
    sofa_first_half_home_big_chances, 
    sofa_first_half_away_big_chances, 
    sofa_first_half_home_big_chances_scored, 
    sofa_first_half_away_big_chances_scored, 
    sofa_first_half_home_big_chances_missed, 
    sofa_first_half_away_big_chances_missed, 
    sofa_second_half_home_big_chances, 
    sofa_second_half_away_big_chances, 
    sofa_second_half_home_big_chances_scored, 
    sofa_second_half_away_big_chances_scored, 
    sofa_second_half_home_big_chances_missed, 
    sofa_second_half_away_big_chances_missed
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_big_chances, 
    st.sofascore_all_away_big_chances, 
    st.sofascore_all_home_big_chances_scored, 	
    st.sofascore_all_away_big_chances_scored, 
    st.sofascore_all_home_big_chances_missed, 
    st.sofascore_all_away_big_chances_missed, 
    st.sofascore_first_half_home_big_chances, 
    st.sofascore_first_half_away_big_chances, 
    st.sofascore_first_half_home_big_chances_scored, 
    st.sofascore_first_half_away_big_chances_scored, 
    st.sofascore_first_half_home_big_chances_missed, 
    st.sofascore_first_half_away_big_chances_missed, 
    st.sofascore_second_half_home_big_chances, 
    st.sofascore_second_half_away_big_chances, 
    st.sofascore_second_half_home_big_chances_scored, 
    st.sofascore_second_half_away_big_chances_scored, 
    st.sofascore_second_half_home_big_chances_missed, 
    st.sofascore_second_half_away_big_chances_missed
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_offsides
INSERT INTO scottish_premiership.dim_offsides (
    game_id, 
    sofa_all_home_offsides, 
    sofa_all_away_offsides, 
    sofa_first_half_home_offsides, 
    sofa_first_half_away_offsides, 
    sofa_second_half_home_offsides, 
    sofa_second_half_away_offsides, 
    fbref_hometeam_offsides, 
    fbref_awayteam_offsides
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_offsides, 
    st.sofascore_all_away_offsides, 
    st.sofascore_first_half_home_offsides, 
    st.sofascore_first_half_away_offsides, 
    st.sofascore_second_half_home_offsides, 
    st.sofascore_second_half_away_offsides, 
    st.fbref_match_reports_hometeam_offsides, 
    st.fbref_match_reports_awayteam_offsides
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


--dim_tackles
INSERT INTO scottish_premiership.dim_tackles (
    game_id, 
    sofa_all_home_tackles	, 
    sofa_all_away_tackles, 
    sofa_all_home_tackles_won, 
    sofa_all_away_tackles_won, 
    sofa_all_home_total_tackles, 
    sofa_all_away_total_tackles, 
    sofa_first_half_home_tackles, 
    sofa_first_half_away_tackles, 
    sofa_first_half_home_tackles_won, 
    sofa_first_half_away_tackles_won, 
    sofa_first_half_home_total_tackles, 
    sofa_first_half_away_total_tackles, 
    sofa_second_half_home_tackles, 
    sofa_second_half_away_tackles, 
    sofa_second_half_home_tackles_won, 
    sofa_second_half_away_tackles_won, 
    sofa_second_half_home_total_tackles, 
    sofa_second_half_away_total_tackles
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_tackles	,
    st.sofascore_all_away_tackles ,
    st.sofascore_all_home_tackles_won,
    st.sofascore_all_away_tackles_won,
    st.sofascore_all_home_total_tackles,
    st.sofascore_all_away_total_tackles,
    st.sofascore_first_half_home_tackles,
    st.sofascore_first_half_away_tackles,
    st.sofascore_first_half_home_tackles_won,
    st.sofascore_first_half_away_tackles_won,
    st.sofascore_first_half_home_total_tackles,
    st.sofascore_first_half_away_total_tackles,
    st.sofascore_second_half_home_tackles,
    st.sofascore_second_half_away_tackles,
    st.sofascore_second_half_home_tackles_won,
    st.sofascore_second_half_away_tackles_won,
    st.sofascore_second_half_home_total_tackles,
    st.sofascore_second_half_away_total_tackles
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;		


--dim_duels
INSERT INTO scottish_premiership.dim_duels (
    game_id, 
    sofa_all_home_duels	, 
    sofa_all_away_duels, 
    sofa_all_home_ground_duels, 
    sofa_all_away_ground_duels	, 
    sofa_all_home_aerial_duels, 
    sofa_all_away_aerial_duels, 
    sofa_first_half_home_duels, 
    sofa_first_half_away_duels, 
    sofa_first_half_home_ground_duels, 
    sofa_first_half_away_ground_duels, 
    sofa_first_half_home_aerial_duels, 
    sofa_first_half_away_aerial_duels, 
    sofa_second_half_home_duels, 
    sofa_second_half_away_duels, 
    sofa_second_half_home_ground_duels, 
    sofa_second_half_away_ground_duels, 
    sofa_second_half_home_aerial_duels, 
    sofa_second_half_away_aerial_duels
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_duels,	
    st.sofascore_all_away_duels,
    st.sofascore_all_home_ground_duels,
    st.sofascore_all_away_ground_duels	,
    st.sofascore_all_home_aerial_duels,
    st.sofascore_all_away_aerial_duels,
    st.sofascore_first_half_home_duels,
    st.sofascore_first_half_away_duels,
    st.sofascore_first_half_home_ground_duels,
    st.sofascore_first_half_away_ground_duels,
    st.sofascore_first_half_home_aerial_duels,
    st.sofascore_first_half_away_aerial_duels,
    st.sofascore_second_half_home_duels,
    st.sofascore_second_half_away_duels,
    st.sofascore_second_half_home_ground_duels,
    st.sofascore_second_half_away_ground_duels,
    st.sofascore_second_half_home_aerial_duels,
    st.sofascore_second_half_away_aerial_duels
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;	

--dim_dribbles
INSERT INTO scottish_premiership.dim_dribbles (
    game_id, 
    sofa_all_home_dribbles,
    sofa_all_away_dribbles,
    sofa_first_half_home_dribbles,
    sofa_first_half_away_dribbles,
    sofa_second_half_home_dribbles,	
    sofa_second_half_away_dribbles
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_dribbles,
    st.sofascore_all_away_dribbles,
    st.sofascore_first_half_home_dribbles,
    st.sofascore_first_half_away_dribbles,
    st.sofascore_second_half_home_dribbles,	
    st.sofascore_second_half_away_dribbles
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_clearances
INSERT INTO scottish_premiership.dim_clearances (
    game_id, 
    sofa_all_home_clearances,
    sofa_all_away_clearances,
    sofa_first_half_home_clearances,
    sofa_first_half_away_clearances,
    sofa_second_half_home_clearances,
    sofa_second_half_away_clearances
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_clearances,
    st.sofascore_all_away_clearances,
    st.sofascore_first_half_home_clearances,
    st.sofascore_first_half_away_clearances,
    st.sofascore_second_half_home_clearances,
    st.sofascore_second_half_away_clearances
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


--dim_recoveries
INSERT INTO scottish_premiership.dim_recoveries (
    game_id, 
    sofa_all_home_recoveries	,
    sofa_all_away_recoveries,
    sofa_first_half_home_recoveries,
    sofa_first_half_away_recoveries,
    sofa_second_half_home_recoveries,
    sofa_second_half_away_recoveries
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_recoveries,	
    st.sofascore_all_away_recoveries,
    st.sofascore_first_half_home_recoveries,
    st.sofascore_first_half_away_recoveries,
    st.sofascore_second_half_home_recoveries,
    st.sofascore_second_half_away_recoveries
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_free_kicks
INSERT INTO scottish_premiership.dim_free_kicks (
    game_id, 
    sofa_all_home_free_kicks,	
    sofa_all_away_free_kicks,
    sofa_first_half_home_free_kicks,
    sofa_first_half_away_free_kicks,
    sofa_second_half_home_free_kicks,
    sofa_second_half_away_free_kicks
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_free_kicks,	
    st.sofascore_all_away_free_kicks,
    st.sofascore_first_half_home_free_kicks,
    st.sofascore_first_half_away_free_kicks,
    st.sofascore_second_half_home_free_kicks,
    st.sofascore_second_half_away_free_kicks
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_interceptions
INSERT INTO scottish_premiership.dim_interceptions (
    game_id, 
    sofa_all_home_interceptions,	
    sofa_all_away_interceptions,
    sofa_first_half_home_interceptions,
    sofa_first_half_away_interceptions,
    sofa_second_half_home_interceptions,
    sofa_second_half_away_interceptions
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_interceptions,	
    st.sofascore_all_away_interceptions,
    st.sofascore_first_half_home_interceptions,
    st.sofascore_first_half_away_interceptions,
    st.sofascore_second_half_home_interceptions,
    st.sofascore_second_half_away_interceptions
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_goals
INSERT INTO scottish_premiership.dim_goals (
    game_id, 
    sofa_incident_type_goal,
    fbref_goal_list
)
SELECT 
    dg.game_id, 
    st.sofascore_incident_type_goal,	
    st.fbref_match_reports_goal_list
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_final_third_entries
INSERT INTO scottish_premiership.dim_final_third_entries (
    game_id, 
    sofa_all_home_final_third_entries	,
    sofa_all_away_final_third_entries,
    sofa_first_half_home_final_third_entries,
    sofa_first_half_away_final_third_entries,
    sofa_second_half_home_final_third_entries,
    sofa_second_half_away_final_third_entries
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_final_third_entries,	
    st.sofascore_all_away_final_third_entries,
    st.sofascore_first_half_home_final_third_entries,
    st.sofascore_first_half_away_final_third_entries,
    st.sofascore_second_half_home_final_third_entries,
    st.sofascore_second_half_away_final_third_entries
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_throw_ins
INSERT INTO scottish_premiership.dim_throw_ins (
    game_id, 
    sofa_all_home_throw_ins	,
    sofa_all_away_throw_ins,
    sofa_first_half_home_throw_ins,
    sofa_first_half_away_throw_ins,
    sofa_second_half_home_throw_ins,
    sofa_second_half_away_throw_ins
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_throw_ins,	
    st.sofascore_all_away_throw_ins,
    st.sofascore_first_half_home_throw_ins,
    st.sofascore_first_half_away_throw_ins,
    st.sofascore_second_half_home_throw_ins,
    st.sofascore_second_half_away_throw_ins
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_incidents_rest
INSERT INTO scottish_premiership.dim_incidents_rest (
    game_id, 
    sofa_incident_type_period,
    sofa_incidents
)
SELECT 
    dg.game_id, 
    st.sofascore_incident_type_period,
    st.sofascore_incidents
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;


--dim_goal_kicks
INSERT INTO scottish_premiership.dim_goal_kicks (
    game_id, 
    sofa_all_home_goal_kicks	,
    sofa_all_away_goal_kicks,
    sofa_first_half_home_goal_kicks,
    sofa_first_half_away_goal_kicks,
    sofa_second_half_home_goal_kicks,
    sofa_second_half_away_goal_kicks
)
SELECT 
    dg.game_id, 
    st.sofascore_all_home_goal_kicks,	
    st.sofascore_all_away_goal_kicks,
    st.sofascore_first_half_home_goal_kicks,
    st.sofascore_first_half_away_goal_kicks,
    st.sofascore_second_half_home_goal_kicks,
    st.sofascore_second_half_away_goal_kicks
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;

--dim_penalties
INSERT INTO scottish_premiership.dim_penalties (
    game_id, 
    fbref_hometeam_pkatt,
    fbref_hometeam_pka,
    fbref_hometeam_pksv,
    fbref_hometeam_pkm,
    fbref_awayteam_pkatt,
    fbref_awayteam_pka,
    fbref_awayteam_pksv,
    fbref_awayteam_pkm,
    fbref_missed_penalty_list
)
SELECT 
    dg.game_id, 
    st.fbref_only_general_stats_goalkeeping_hometeam_pkatt,
    st.fbref_only_general_stats_goalkeeping_hometeam_pka,
    st.fbref_only_general_stats_goalkeeping_hometeam_pksv,
    st.fbref_only_general_stats_goalkeeping_hometeam_pkm,
    st.fbref_only_general_stats_goalkeeping_awayteam_pkatt,
    st.fbref_only_general_stats_goalkeeping_awayteam_pka,
    st.fbref_only_general_stats_goalkeeping_awayteam_pksv,
    st.fbref_only_general_stats_goalkeeping_awayteam_pkm,
    st.fbref_match_reports_missed_penalty_list
FROM 
    scottish_premiership.staging_table_fl st
JOIN 
    scottish_premiership.dim_general_info dg 
ON 
    st.game_date = dg.game_date AND st.hometeam = dg.hometeam
ON CONFLICT (game_id) DO NOTHING;




