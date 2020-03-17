newTerminal()
{
	subprocess.call(['xterm', '-e', $1])
}

TEAM_NAME_ONE="Kuntz"
TEAM_NAME_TWO="Jon"

newTerminal 'python player.py TEAM_NAME_ONE 50 10 goalie'
python player.py TEAM_NAME_ONE 10 10
#python player.py team1Name x y
#python player.py team1Name x y
#python player.py team1Name x y
#python player.py team1Name x y

python player.py TEAM_NAME_TWO 10 10 goalie
#python player.py team2Name x y
#python player.py team2Name x y
#python player.py team2Name x y
#python player.py team2Name x y
#python player.py team2Name x y
