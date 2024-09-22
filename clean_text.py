import re
import string

# Sample long text
text = """Tell me where to go tell me what to do I'll be right there for you Tell me what to say no matter if it's true I'll say it all for you  I used to be the type of kid that would always think the sky is falling Why am I so differently wired? Am I a martian? What kind of twisted experiment am I involved in? 'Cause I don't belong in this world That's why I'm scoffing at authority defiant often Flying off at the handle at my mom no dad So I am non-compliant at home at school I'm just shy and awkward And I don't need no goddamn psychologist Tryna diagnose why I have all these underlying problems Thinking he can try and solve them I'm outside chalking up drawings on the sidewalk And in the front drive talking to myself Either that or inside hiding off in the corner somewhere quiet Trying not to be noticed 'cause I'm crying and sobbing I had a bad day at school so I ain't talking Some cocksucker shoved me into a fucking locker 'Cause he said that I eyeballed him  And if you fall I'll get you there I'll be your savior from all the wars that are fought Inside your world Please have faith in my words  'Cause this is my legacy legacy eh This is my legacy legacy eh There's no guarantee It's not up to me We can only see This is my legacy legacy Legacy legacy  I used to be the type of kid that would always think the sky is falling Why am I so differently wired in my noggin? 'Cause sporadic as my thoughts come it's mind boggling 'Cause I obsess on everything in my mind small shit Bothers me but not my father he said Sayonara then split But I don't give a shit I'm fine long as There's batteries in my Walkman nothing's the matter with me Shit look on the bright side at least I ain't walking I bike ride through the neighborhood of my apartment Complex on a ten speed which I've acquired parts that I Find in the garbage a frame then put tires on it Headphones on look straight ahead if kids try and start shit But if this is all there is for me life offers Why bother even try and put up a fight it's nonsense But I think a light bulb just lit up in my conscience What about them rhymes I've been jottin' They're kinda giving me confidence Instead of tryna escape through my comics Why don't I just blast a little something like Onyx To put me in the mood to wanna fight and write songs that Say what I wanna say to the kid that said that I eyeballed him Grab hold of my balls like that's right fight's on bitch Who would've knew from the moment I turned the mic on that I could be iconic in my conquest That's word to Phife Dawg from a tribe called Quest  This is my legacy legacy eh This is my legacy legacy eh There's no guarantee It's not up to me We can only see This is my legacy legacy Legacy legacy  I used to be the type of kid that would always think the sky is falling Now I think the fact that I'm differently wired's awesome 'Cause if I wasn't I wouldn't be able to work Words like this and connect lines like crosswords And use my enemy's words as strength To try and draw from and get inspired off em 'Cause all my life I was told and taught I am not shit By you wack fucking giant sacks of lying dog shit Now you shut up bitch I am talking Thought I was full of horseshit and now You fucking worship the ground on which I am walking Me against the world so what? I'm Brian Dawkins Versus the whole 0 and 16 Lions offense So bring on the Giants Falcons and Miami Dolphins It's the body bag game bitch I'm supplying coffins 'Cause you dicks butt kiss a bunch of Brian Baldingers You gon' die a ball licker I've been diabolical With this dialogue since 99 Rawkus You don't respect the legacy I leave behind y'all can Suck a dick the day you beat me pigs'll fly out my ass In a flying saucer full of Italian sausage The most high exalting and I ain't halting 'Til I die of exhaustion inhale my exhaust fumes The best part about me is I am not you I'm me and I'm the Fire Marshall and this is my  Legacy legacy eh This is my legacy legacy eh There's no guarantee it's not up to me we can only see This is my legacy legacy Legacy legacy"""


# Function to clean and limit text to 514 words
def clean_and_limit_text(text):
    # Remove punctuation using string.punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra spaces
    text = re.sub(' +', ' ', text)  # Replace multiple spaces with a single space
    
    # Remove any remaining symbols (e.g., #, $, %, &)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    
    # Strip leading/trailing spaces
    text = text.strip()
    
    # Split text into words
    words = text.split()
    
    limited_text = ' '.join(words)
    
    return limited_text

# Cleaned and limited text
cleaned_text = clean_and_limit_text(text)
print(cleaned_text)
