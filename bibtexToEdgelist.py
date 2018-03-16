from pybtex.database import parse_file
import sys

reload(sys)
sys.setdefaultencoding('utf8')

bib_data = parse_file('scopus.bib')

# print bib_data.entries

#function that extracts all possible couples from a list
def get_pairs(lst):
    if len(lst) < 2:
        return lst
    result = []
    for x in range(len(lst)):
        for y in range(x+1,len(lst)):
            result.append([lst[x],lst[y]])
    return result

def make_edge_list(title, pairs):
    for pair in pairs:
        #print pair
        strpair = ','.join(pair)
        result = title + "," + strpair.lower() + "\n"
        print result
        with open("Output.txt", "a") as text_file:
            text_file.write(result)

all_keyword_lists = [];
#print bib_data.entries['Cesar2013'].fields['title']
for entry_id in bib_data.entries:
    entry = bib_data.entries[entry_id].fields
    try:
        #print entry["keywords"]
        keyword_str = entry["keywords"].replace("; ", ",")
        keyword_str = keyword_str.replace(", ", ",")
        keyword_list = keyword_str.split(",")
        print "number of keywords = " + str(len(keyword_list));
        print "number of pairs = %s" % len(get_pairs(keyword_list))
        #give keyword pairs and title for making an edge list
        make_edge_list(entry_id, get_pairs(keyword_list))
        #print entry_id
        all_keyword_lists.append(keyword_list)
    except(KeyError):
        continue

print len(bib_data.entries)

print "Printing pairs.."
for i in all_keyword_lists:
    #print all_pairs(all_keyword_lists[i])
    print len(get_pairs(i))

zoo_animals = ["pangolin", "cassowary", "sloth", "chicken"];
# One animal is missing!

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the "  + zoo_animals[0]
  print "The second animal at the zoo is the "  + zoo_animals[1]
  print "The third animal at the zoo is the  " + zoo_animals[2]
  print "The fourth animal at the zoo is the  " + zoo_animals[3]
