# RPM Spec Files for Popular Neuroimaging Suites
===============

## Description

I'm basically using this repo to experiment around with RPM packaging.  I'm particularly interested
in the packaging of scientific computing software, since I see this as a key element in increasing
the reproducility of scientific analyses (see [here](https://libjpel.so/scientific-archivability.html) for
my ramblings on this topic).  Presently, this repo only has a spec file for AFNI, which is not
really quite packaged in the ideal manner (there should be a build step w/ a Makefile).  Right now,
the spec file downloads a pre-compiled binary and puts it in /usr/local/afni (possibly not the best spot, but I'll
have to read the [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) over a bit more to see
if maybe I should put it somewhere else.  I haven't tested it yet, but if it doesn't suck / commit some heresy,
I might try to get it in [NeuroFedora](https://fedoraproject.org/wiki/SIGs/NeuroFedora).

## Special Instructions

The build command depends on a variable definition for the version number (which in turn comes from a `curl` command):

```
rpmbuild -bb --define "_afniver $(/usr/bin/curl -S https://afni.nimh.nih.gov/pub/dist/AFNI.version --silent | /bin/head -1 | /bin/cut -d_ -f2)" afni.spec
```

On CentOS 7, you'll need to [edit /etc/rpm/macros.dist](https://cstan.io/?p=8946&lang=en).

I'm a bit iffy about defining the path for AFNI in `/etc/profile.d` ; I seem to remember this causing issues with non-login shells that wanted to use AFNI.
