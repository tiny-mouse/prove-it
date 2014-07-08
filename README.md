prove-it
========

A repo to flex your testing skills.  It's intentionally broken, let's see if you can fix it.


Setup
=====
pip install virtualenv
mkdir env
virtualenv env
source env/bin/activate
pip install -r requirements.txt


Running the tests
======================
Just run `nosetests` in your terminal where this code lives with
the virtualenv activated

Note: If you want to see what happens when the integration tests are run
without cassette, just move the responses file out of the way (aka delete it)



Things TODO:
============
1. Figure out how to fix the test suite.
2. Figure out how to make a decorator out of the argument checking and response formatting in the views file so we can be DRY.


Caveats:
========
1. I'm not entirely sure you can expect request params to be ordered in any way, but I think it's ok for this example.
2. You should realistically have all your view tests be full unit tests and 
   mock out the calculator module, but this is a learning moment, so some of 
   them aren't.
