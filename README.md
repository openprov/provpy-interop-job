# ProvPy Interoperability Tests

[ProvPy](https://github.com/trungdong/prov) interoperability test job.

[![Build Status](https://travis-ci.org/mikej888/provtoolsuite-provpy-interop-job.svg)](https://travis-ci.org/mikej888/provtoolsuite-provpy-interop-job)

The Travis CI test job:

* Gets ProvPy from GitHub (latest master version).
* Gets canonical [test cases](https://github.com/mikej888/provtoolsuite-testcases) from GitHub (stable master branch).
* Gets [interoperability test harness](https://github.com/mikej888/provtoolsuite-interop-test-harness) from GitHub (stable master branch).
* Configures interoperability test harness.
* Runs interoperability tests to validate ProvPy conversions done using prov-convert. Conversions are validated using ProvPy's prov-compare script.

## Author

Developed by [The Software Sustainability Institute](http://www.software.ac.uk>) and the [Provenance Tool Suite](http://provenance.ecs.soton.ac.uk/) team at [Electronics and Computer Science](http://www.ecs.soton.ac.uk) at the [University of Southampton](http://www.soton.ac.uk).

For more information, see our [document repository](https://github.com/prov-suite/ssi-consultancy/).

## License

These tests are released under the MIT license.
