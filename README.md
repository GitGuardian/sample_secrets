# sample_secrets

## Introduction

GitGuardian offers the possibility to **scan your repositories' entire git history for [secrets](https://www.gitguardian.com/secrets-detection)**, across all git branches.

This repository contains sample secrets for testing purposes. Our recommended procedure is to:
1. **Fork this repository** to your GitHub user account or to a GitHub organization where you are admin.
2. [**Sign up to GitGuardian**](https://dashboard.gitguardian.com/auth/signup) for free if you haven't already.
3. **Integrate** your GitHub user (or GitHub organization) within GitGuardian.
4. Once the repos are being monitored by GitGuardian, you **can scan their git history** via the [Perimeter page](https://dashboard.gitguardian.com/perimeter)
5. **The [secrets incidents](https://www.gitguardian.com/secrets-detection) uncovered by GitGuardian** will be visible in the [Incidents page](https://dashboard.gitguardian.com/incidents/secrets).

## What types of secrets will you find in this repository

Before going further, be aware that **a single secret can be seen in multiple places within a repository**. We refer to them as **occurrences** of the secret. GitGuardian groups these occurrences under the same secret incident.

=> **A secret incident can have multiple occurrences**. This allows you to understand how you might be affected by [secret sprawl](https://blog.gitguardian.com/secret-sprawl/).

| Secret detector        | Secret           | # of occurrences  |
| ------------- |:-------------| -----:|
| AWS keys    | `hjshXXXXXXXXXXXXXXXXXXsjkja`| 1 |
| MongoDB URI      | `hub2XXXoeu`      | 3 |
| PostgreSQL Credentials | `sup3XXXXXXXXXorGG`      |  2 |
| Generic High Entropy Secret | `ezkjXXXXXXXXXXXXXXXXXzhnze`      |  1 |
| Generic High Entropy Secret | `mrglXXXXXXXXXXXXXXXXXX2Z3Y`      |  1 |
| RSA Private Key | `MIIEXXXXXXX......XXXXXXXXg4wA=`      |  1 |
| SMTP credentials | `OhYeXXXXXXXXXXXtPas`      |  1 |
| LDAP credentials | `k%udXXXXXXXXX8=H_`      |  1 |

Of course, these are not the only types of secrets that we support. You can find an exhaustive list of our detectors in our [secrets detection engine documentation](https://docs.gitguardian.com/secrets-detection/home).


> :owl: [GitGuardian](https://www.gitguardian.com/) is an automated secrets detection service.
We help developers and security teams secure the modern software development process.
