def starting_elevens(home_players_list_param,away_players_list_param,substitutions_param):
    try:
        dict_starting_elevens = dict()
        home_players_slug_names =[]
        for player_home in home_players_list_param:
            home_players_slug_names.append(player_home["player_slug"])

        away_players_slug_names =[]
        for player_away in away_players_list_param:
            away_players_slug_names.append(player_away["player_slug"])

        #substitutions_update
        for substituion_eintrag in substitutions_param:
            team_dict =  dict()
            #print(substituion_eintrag["in"]["playerIn_name_slug"])
            if substituion_eintrag["in"]["playerIn_name_slug"] in home_players_slug_names:
                team_dict["team"] = "home"
            else:
                team_dict["team"] = "away"
            substituion_eintrag["in"]["team"] = team_dict["team"]
            team_dict =  dict()
            #print(substituion_eintrag["out"]["playerOut_name_slug"])
            if substituion_eintrag["out"]["playerOut_name_slug"] in home_players_slug_names:
                #print("home")
                team_dict["team"] = "home"
            else:
                #print("away")
                team_dict["team"] = "away"
            substituion_eintrag["out"]["team"] = team_dict["team"]


        #HOME

        starting_eleven_players_home = []
        home_from_bench__players = []
        for pl in  substitutions_param:
            if pl["in"]["team"] == "home":
                home_from_bench__players.append(pl)

        home_players_have_played = []
        for player_has_played in home_players_list_param:
            if player_has_played["player_has_played"] == 1:
                home_players_have_played.append(player_has_played)




        home_players_have_player_only_names = []
        for j in home_players_have_played:
            home_players_have_player_only_names.append(j["player_slug"])




        home_from_bench_players_only_names = []
        for l in home_from_bench__players:
            home_from_bench_players_only_names.append(l["in"]["playerIn_name_slug"])



        for m in home_players_have_played:
            if m["player_slug"] not in home_from_bench_players_only_names:
                starting_eleven_players_home.append(m)


        #AWAY
        starting_eleven_players_away = []
        away_from_bench__players = []
        for pl in  substitutions_param:
            if pl["in"]["team"] == "away":
                away_from_bench__players.append(pl)

        away_players_have_played = []
        for player_has_played in away_players_list_param:
            if player_has_played["player_has_played"] == 1:
                away_players_have_played.append(player_has_played)




        away_players_have_player_only_names = []
        for j in away_players_have_played:
            away_players_have_player_only_names.append(j["player_slug"])




        away_from_bench_players_only_names = []
        for l in away_from_bench__players:
            away_from_bench_players_only_names.append(l["in"]["playerIn_name_slug"])



        for m in away_players_have_played:
            if m["player_slug"] not in away_from_bench_players_only_names:
                starting_eleven_players_away.append(m)
    except:
        starting_eleven_players_home = None
        starting_eleven_players_away = None
    
    dict_starting_elevens["home_starting_eleven"] = starting_eleven_players_home
    dict_starting_elevens["away_starting_eleven"] = starting_eleven_players_away
    return dict_starting_elevens
    