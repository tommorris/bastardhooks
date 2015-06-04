## Bastardhooks

Bastardhooks is a collection of [pre-commit framework](http://pre-commit.com) hooks to enforce code style preferences of mean, vicious bastards.

Hooks provided include:

* `no_coffee`: prevents the check-in of CoffeeScript code based on a [slightly irrational dislike of the language](https://tommorris.org/posts/9029)
* `no_stupid_php`: checks to see if the user has attempted to use any particularly idiotic things in PHP (like [`magic_quotes`](http://php.net/manual/en/security.magicquotes.php))
