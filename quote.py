from re import split

class Quote:
    def __init__(self, quote, author, birth, bio):
        self.quote = quote
        self.author = author
        self.birth = birth
        self.bio = bio
    def get_initials(self):
        names = split(r"\W+", self.author)
        initials=""
        for name in names:
            initials += name[0]
        return initials
    def bio_without_author_name(self):
        new_bio = self.bio
        for name in self.author.split(" "):
            new_bio = new_bio.replace(name, "*")
        return new_bio

if __name__ == "__main__":
    bio = "See also: Robert GalbraithAlthough she writes under the pen name J.K. Rowling, pronounced like rolling, her name when her first Harry Potter book was published was simply Joanne Rowling. Anticipating that the target audience of young boys might not want to read a book written by a woman, her publishers demanded that she use two initials, rather than her full name. As she had no middle name, she chose K as the second initial of her pen name, from her paternal grandmother Kathleen Ada Bulgen Rowling. She calls herself Jo and has said, \"No one ever called me 'Joanne' when I was young, unless they were angry.\" Following her marriage, she has sometimes used the name Joanne Murray when conducting personal business. During the Leveson Inquiry she gave evidence under the name of Joanne Kathleen Rowling. In a 2012 interview, Rowling noted that she no longer cared that people pronounced her name incorrectly.Rowling was born to Peter James Rowling, a Rolls-Royce aircraft engineer, and Anne Rowling (née Volant), on 31 July 1965 in Yate, Gloucestershire, England, 10 miles (16 km) northeast of Bristol. Her mother Anne was half-French and half-Scottish. Her parents first met on a train departing from King's Cross Station bound for Arbroath in 1964. They married on 14 March 1965. Her mother's maternal grandfather, Dugald Campbell, was born in Lamlash on the Isle of Arran. Her mother's paternal grandfather, Louis Volant, was awarded the Croix de Guerre for exceptional bravery in defending the village of Courcelles-le-Comte during the First World War.Rowling's sister Dianne was born at their home when Rowling was 23 months old. The family moved to the nearby village Winterbourne when Rowling was four. She attended St Michael's Primary School, a school founded by abolitionist William Wilberforce and education reformer Hannah More. Her headmaster at St Michael's, Alfred Dunn, has been suggested as the inspiration for the Harry Potter headmaster Albus Dumbledore.As a child, Rowling often wrote fantasy stories, which she would usually then read to her sister. She recalls that: \"I can still remember me telling her a story in which she fell down a rabbit hole and was fed strawberries by the rabbit family inside it. Certainly the first story I ever wrote down (when I was five or six) was about a rabbit called Rabbit. He got the measles and was visited by his friends, including a giant bee called Miss Bee.\" At the age of nine, Rowling moved to Church Cottage in the Gloucestershire village of Tutshill, close to Chepstow, Wales. When she was a young teenager, her great aunt, who Rowling said \"taught classics and approved of a thirst for knowledge, even of a questionable kind,\" gave her a very old copy of Jessica Mitford's autobiography, Hons and Rebels. Mitford became Rowling's heroine, and Rowling subsequently read all of her books.Rowling has said of her teenage years, in an interview with The New Yorker, \"I wasn’t particularly happy. I think it’s a dreadful time of life.\" She had a difficult homelife; her mother was ill and she had a difficult relationship with her father (she is no longer on speaking terms with him). She attended secondary school at Wyedean School and College, where her mother had worked as a technician in the science department. Rowling said of her adolescence, \"Hermione [a bookish, know-it-all Harry Potter character] is loosely based on me. She's a caricature of me when I was eleven, which I'm not particularly proud of.\" Steve Eddy, who taught Rowling English when she first arrived, remembers her as \"not exceptional\" but \"one of a group of girls who were bright, and quite good at English.\" Sean Harris, her best friend in the Upper Sixth owned a turquoise Ford Anglia, which she says inspired the one in her books."


    q = Quote("ciao bello", "J.K. Rowling", "Born: July 31, 1965 in Yate, South Gloucestershire, England, The United Kingdom", bio)

    print(q.get_initials())
    print(q.bio_without_author_name())