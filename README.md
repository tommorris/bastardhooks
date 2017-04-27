## Bastardhooks

Bastardhooks is a collection of [pre-commit framework](http://pre-commit.com) hooks to enforce code style preferences of mean, vicious bastards.

Hooks provided include:

* `check_for_rspec_focus`: ensures that you don't check in RSpec tests that have focus words (e.g. `fscenario`)
* `no_coffee`: prevents the check-in of CoffeeScript code based on a [slightly irrational dislike of the language](https://tommorris.org/posts/9029)
* `no_stupid_php`: checks to see if the user has attempted to use any particularly idiotic things in PHP (like [`magic_quotes`](http://php.net/manual/en/security.magicquotes.php))
* `secrets`: checks to see if there's anything from your `~/.secrets` file being checked in. This is to replicate the functionality of [git-secrets](https://github.com/awslabs/git-secrets) but with less effort.
