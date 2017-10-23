import json

def main():
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highest=0
    county = ""
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highest:
            highest = c["Age"]["Percent Under 18 Years"]
            county = c["County"] + ", " + c["State"]
    return county
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest=0
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highest:
            highest = c["Age"]["Percent Under 18 Years"]
    return highest
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    result = ["", 0]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > result[1]:
            result[1] = c["Age"]["Percent Under 18 Years"]
            result[0] = c["County"] + ", " + c["State"]
    return result
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    states={}
    for c in counties:
        if c["State"] in states:
            states[c["State"]] += 1
        else:
            states[c["State"]] = 1
    #Find the state in the dictionary with the most counties
    highest = 0
    state = ""
    for s in states:
        if states[s] > highest:
            highest = states[s]
            state = s
    #Return the state with the most counties
    return state
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()
