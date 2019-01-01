from typing import NamedTuple, Tuple, DefaultDict, Dict, List
from kmeans import k_means, assign_data
import csv
from collections import namedtuple, defaultdict, Counter
from pprint import pprint
import glob

# We are using glob to be able to use filename as wild card and loop 
# Troughout all csv files in the directory
# Creating a structure for the data
# Load votes whick were arranged by topic and accumulate votes by senator
# Use alias for int
NUM_SENATORS = 100
VoteValue = int
VoteHistory = Tuple[VoteValue, ...]
vote_value = {'Yea': 1, 'Aye': 1, 'Nay': -1, 'No': -1, 'Not Voting': 0, 'Present': 0}     # type: Dict[str, VoteValue]

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
# Senator = namedtuple('Senator', ['name', 'party', 'state'])

accumulated_record = defaultdict(list)                                      # type: DefaultDict[Senator, List[VoteValue]]
for filename in glob.glob('CSVs/congress*.csv'):
	with open(filename, encoding='utf-8') as f:
	    reader = csv.reader(f)
	    ## read two lines in ones
	    vote_topic = next(reader)
	    headers = next(reader)
	    # Read whole line in varialbes
	    for person, state, district, vote, name, party in reader:
	    	senator = Senator(name, party, state)
	    	accumulated_record[senator].append(vote_value[vote])

# Transform the record into a plain dict taht maps to tuple of votes
# Using dictionary comprehanssion
# senator that maps to tuple of the votes for each senator and list of votes 

# record is a dictionary that maps a senator to voting history
record = {senator: tuple(votes) for senator, votes in accumulated_record.items()}   # type: Dict[Senator, VoteHistory]

# Use k-means to locate the cluster centroids from pattern of votes, assign each senator to the nearest cluster
centroids = k_means(record.values(), k=4)
clustered_votes = assign_data(centroids, record.values())

# Build a revers mapping from a vote history to a list of senators who voted that way
# Maps the voting history to list of senators. Key to defautl dict is VoteHistory and value is list of Senators
votes_to_senators = defaultdict(list)       # type: DefaultDict[VoteHistory, List[Senator]]  
for senator, votehistory in record.items():
    votes_to_senators[votehistory].append(senator)

# assert sum(len(cluster) for cluster in votes_to_senators.values()) == NUM_SENATORS

# Display the clusters and the members (senators) of each cluster
mystr='='*20
for i, votes_in_cluster in enumerate(clustered_votes.values(), start=1):
    print (f'\n{mystr} Voting Cluster #{i} {mystr}')
    party_totals = Counter()
    for votes in set(votes_in_cluster):
        for senator in votes_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)
