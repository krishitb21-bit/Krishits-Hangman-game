import random

words = (
    'galaxy', 'nebula', 'python', 'matrix', 'wizard', 'safari', 'jungle', 'crypto', 'shadow', 'biscuit',
    'avalanche', 'blizzard', 'horizon', 'phantom', 'odyssey', 'subway', 'rhythm', 'oxygen', 'vampire', 'coconut',
    'ability', 'absence', 'academy', 'account', 'accuse', 'achieve', 'acquire', 'actions', 'actress', 'adapter',
    'address', 'advance', 'advisor', 'against', 'airline', 'airport', 'alchemy', 'alcohol', 'algebra', 'alleged',
    'allergy', 'allowed', 'almond', 'already', 'alright', 'altered', 'amazing', 'ambient', 'ammonia', 'analyst',
    'anatomy', 'ancestor', 'anchors', 'ancient', 'android', 'animals', 'answers', 'antenna', 'anxiety', 'anybody',
    'anyways', 'apartment', 'apology', 'apparel', 'appeals', 'appears', 'appease', 'applaud', 'applied', 'appoint',
    'approve', 'apricot', 'aquatic', 'aquifer', 'arcade', 'archery', 'archive', 'arduous', 'arguing', 'armadillo',
    'arrived', 'artisan', 'artists', 'artwork', 'asbestos', 'asphalt', 'aspires', 'assault', 'assegai', 'asserts',
    'assigns', 'assists', 'assumed', 'assumes', 'assured', 'asterisk', 'asteroid', 'astound', 'asylum', 'athlete',
    'atoll', 'atomic', 'atrium', 'attends', 'attires', 'attract', 'auction', 'audible', 'audited', 'auditor',
    'augment', 'austere', 'authors', 'autopsy', 'autumn', 'avenge', 'avenue', 'average', 'aviator', 'avocado',
    'awakens', 'awarded', 'awesome', 'awkward', 'axioms', 'azimuth', 'baboons', 'backlog', 'backpack', 'badgers',
    'baffled', 'baggage', 'bagpipe', 'balance', 'balcony', 'ballads', 'ballast', 'balloon', 'ballots', 'balsam',
    'bamboos', 'bananas', 'bandage', 'bandana', 'bandits', 'bangles', 'banished', 'banjo', 'bankers', 'banking',
    'banned', 'banners', 'banquet', 'banters', 'baptism', 'barbarian', 'barbecue', 'barbers', 'barcodes', 'barefoot',
    'bargain', 'barges', 'baritone', 'barium', 'barking', 'barleys', 'baroness', 'baroque', 'barracks', 'barrage',
    'barrels', 'barriers', 'barrows', 'barters', 'basalt', 'baseline', 'basements', 'bashful', 'basics', 'basilisk',
    'baskets', 'basking', 'bastion', 'batches', 'bathrobe', 'bathtub', 'battery', 'battled', 'battles', 'beaches',
    'beacons', 'beading', 'beagles')

random_word = random.choice(words).lower()
random_word = list(random_word)

hangman_art = {
    1: """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    2: """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    3: """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    4: """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    5: """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    6: """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    7: """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
}



user_guess = ""
dashes = ['_'] * len(random_word)
assembly = 0
while '_' in dashes:
    user_guess = input("Enter your guess: ")

    if len(user_guess) != 1:
        print("Only one letter allowed.")
    elif user_guess in random_word:
        print('You guessed correctly!')
        position = random_word.index(user_guess)
        for i in range(len(random_word)):
            if random_word[i] == user_guess:
                dashes[i] = user_guess
        print(' '.join(dashes))
    elif user_guess not in random_word:
        print('Incorrect guess, Try again!')
        assembly = assembly + 1
        if assembly < 7:
            print(hangman_art[assembly])
        else:
            print('You lost')
print()
print("You guessed the word!")


















