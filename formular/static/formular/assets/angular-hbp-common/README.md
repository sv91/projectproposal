Angular HBP Common contains common web materials to support creation of
new websites.

Structure
=========

```
- src/
 `- assets/            // contains static assets sources
 `- scripts/           // AngularJS services, directives and controllers
 `- styles/            // Sass styles
- bower_components/  // Bower components
- dist/                // Distributed code
- styleguide-templates // Templates used by kss to generate the Styleguide
```

What's in /dist/ folder
=======================

- Styleguide: a set of HTML webpage that can be called the HBP styleguide
- angular-hbp-common.js: a set of common angular scripts grouped in the hbpCommon module
- hbp-common.css: Twitter Bootstrap and the rules describe in the styleguide

Development
===========

Clone the git repository:

```
git clone ssh://bbpcode.epfl.ch/platform/JSLibAngularHbpCommon
```

Start the development server using

```grunt serve```

Start sever against the compressed assets using

```grunt serve:dist```

Build using grunt

```grunt dist```

The code is run automatically by the watch task from the devel server. To
trigger test manually, run:

```grunt test```

Release
=======

Note: It should be done through Jenking by launching a build with 'release' param set to patch/minor/major.

Steps:
- manually update the version in:
 - bower.json
 - package.json
 - src/angular-hbp-common.js

- commit the 3 files and submit review
```
grunt gitcommit:bump
git review
```
- build project
```
grunt dist
```
- commit result, create version tag and push it to remote
```
grunt gitcommit:dist gittag:dist gitpush:dist
```
- make sure the last commit is not pushed to master:
```
git reset HEAD~1
```

to check that the version is available in bower repository:
```
bower info angular-hbp-common#<version>
```
