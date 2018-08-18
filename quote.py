from re import split


class Quote:
    def __init__(self, quote, author, birth, bio):
        self.quote = quote
        self.author = author
        self.birth = birth
        self.bio = bio

    def __repr__(self):
        return self.quote

    def get_initials(self):
        names = split(r"\W+", self.author)
        initials = ""
        for name in names:
            if name:
                initials += name[0]
        return initials

    def bio_without_author_name(self):
        new_bio = self.bio
        for name in self.author.split(" "):
            new_bio = new_bio.replace(name, "*"*len(name))
        return new_bio
