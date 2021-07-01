from nba_api.stats.endpoints import shotchartdetail

response = shotchartdetail.ShotChartDetail(
	team_id=0,
	player_id=201935,
	season_nullable='2018-19',
	season_type_all_star='Regular Season'
)

content = json.loads(response.get_json())
