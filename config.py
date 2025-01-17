#BOOK SETTINGS
OPENINGBOOK = [{"Name": "London Countergambit", "pgn": "1. d4 d5 2. Bf4 c5"}] 
#add the starting point PGNs you want to create repertoires for, with starting point pgns. The format for multiple PGNs and chapters looks like this: [{"Name": "Book A", "pgn": "1. e4 e5"},{"Name": "Book B", "pgn": "1. e4 e5 2. f4"}]
LONGTOSHORT = 0
#if you want the chapter ordered from long lines to short lines, instead of short to long, change to "1". Else 0.


#DATABASE SETTINGS
VARIANT = 'standard' 
#Variants to include in the analysis
SPEEDS = ['blitz,rapid,classical,correspondence'] 
#comma separated Formats to include in the analysis
RATINGS = ['1600,1800,2000,2200,2500'] 
#Ratings of the players to include in the analysis
MOVES = 10
#The number of most played moves to search over for the best move (minimum 5)

#MOVE SELECTION SETTINGS
DEPTHLIKELIHOOD = 0.01
#this controls how deep moves and lines are generated. The smaller the number the deeper the lines. Once cumulative line likelihood reaches this probability threshold, no futher continuations will be added (in percentage so 0.0025 = 0.25%)
ALPHA = 0.001
#The larger this number the more likely we are to select moves with less data. This is the confidence interval alpha (EG 0.05 = 95% CI), for deciding the lower bounds of how good a move's winrate is.
MINPLAYRATE = 0.001
#minimum frequency for a move to be played in a position to be considered as a 'best move' candidate, as a percentage (0.05= 5%)
MINGAMES = 19 
#games where moves played this or less than this will be discarded (unless top engine move) (25 = 25 games).
CONTINUATIONGAMES = 10 
# games where moves played this or less than this will not be considered a valid continuation (ie we don't want to be inferring cumulative probability or likely lines from tiny amounts of games/1 game)
DRAWSAREWINS = 0
#if you want to count draws as wins, for the win rate calculation, select 1. Else 0.


#ENGINE SETTINGS
ENGINEPATH = r"/Users/AM/Downloads/BookBuilder/Stockfish"
#the filepath where the engine is stored on your computer, so it can be accessed. Keep the 'r' character
CAREABOUTENGINE = 0
#care about engine eval of position or engine finishing = 1, dont care = 0
ENGINEDEPTH = 10
#what depth the engine should evaluate best moves. the higher the depth the longer the evaluation will take.
ENGINEFINISH = 1
#if we want the engine to complete lines to cumulative likelihood where data is insufficient, 1. Otherwise 0, and lines will end where there's no good human data
SOUNDNESSLIMIT = -99
#maximum centipawns we are willing to be down in engine eval, provided the winrate is better (-300 = losing by 3 pawns in eval). We never give up a forced mate, however.
MOVELOSSLIMIT = -99
#maximum centipawns we are willing to lose vs engine analysis pre move to play a higher winrate move. We never give up a forced mate, however.
IGNORELOSSLIMIT = 300
#centipawns advantage above which we won't care if we play a move that hits our loss limit, if it has a higher win rate (is easier to win)
ENGINETHREADS = 1 #my max 20
#how many threads you want the engine to use (check your comp and set 1 if unsure)
ENGINEHASH = 320 #my max 10240
#how much hash you want the engine to use (check your comp and set to 16 if unsure)

