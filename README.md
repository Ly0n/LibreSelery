<img align="middle" src="./docs/OpenSelery-04.png" width="400">

### Automated Contribution Financing

*OpenSelery is a decentralized framework for funding distribution in free software development. It offers transparent, automated and adaptable funding of contributors integrated into Github Action by the [seleryaction](https://github.com/protontypes/seleryaction) template.*

[![](https://img.shields.io/gitter/room/protontypes/openselery)](https://gitter.im/protontypes/openselery)[![](https://img.shields.io/docker/cloud/build/protontypes/openselery?logo=docker)](https://hub.docker.com/r/openselery/openselery)[![stability-experimental](https://img.shields.io/badge/stability-experimental-orange.svg)](https://github.com/emersion/stability-badges#experimental)   

[![Actions Status](https://github.com/protontypes/openselery/workflows/seleryaction/badge.svg)](https://github.com/protontypes/openselery/actions?query=workflow%3Aseleryaction)![Balance](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/wiki/protontypes/openselery/openselery/balance_badge.json&style=flat&logo=bitcoin)![Balance](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/wiki/protontypes/openselery/openselery/native_balance_badge.json&style=flat&logo=bitcoin)      
[![Donate with bitcoin](https://badgen.net/badge/Donate/3PVdiyLPR7MgaeFRJLW9mfuESZS2aAPX9w/orange?icon=bitcoin)](https://github.com/protontypes/openselery/wiki/Donation)
[![Transaction History](https://badgen.net/badge/icon/Transaction%20History?icon=bitcoin&label)](https://github.com/protontypes/openselery/wiki/Transaction-History)

*OpenSelery is a new funding model for digital open projects and in experimental state. The amount of funding on your wallet should therefore be limited.*

## Concept

OpenSelery is a donation distribution system for open source projects that runs decentralized in continuous integration pipelines. 
It is triggered with every push to you master branch and distributes donations between contributors based on an open source metric that is publicly visible.
The project donations splits can be weighted by the following options: 
* Uniform Weight: Everyone who contributed a minimum number of commits to the master branch is considered.
* Activity Weight: Everyone who contributed in the last X commits 
* Issue Contribution: Everybody who created, commented or closed on an Issue that is closed since Y days and has minimum commits
* (More weights are discussed)      

The total amount of donations per push on the master is distributed based on the sum of weights and mailed via the Coinbase API to the public email address on Github. We don't want to send emails to the git commit email addresses to not spam people. 
With our dependency scanning option you can even chose a user defined number of random contributors from your dependency tree and include them to your donation distribution. 

## How it works

1. OpenSelery is configured based on the selery.yml file and runs completely decentralized as a Github Action.
2. Triggers with every push on the master branch.
3. Gathers contributor information about the target project via the Github and Libraries.io API.
4. Filters out contributors with hidden email address in the Github profile and below the mininum contribution limit. 
5. Creates user defined funding distribution weights based on different projects contribution assessment: Minimum Contribution, activity, solved issues, ...
6. Sums the weights together to the combined weight used for different split modes.
7. Splits the funding between contributers based on the chosen mode.
8. Pays out Cryptocurrency to the chosen contributor email addresses via the Coinbase API. Contributors without a Coinbase account will get a email to claim the donation.


<a href="https://asciinema.org/a/353518">
<p align="center">
  <img src="https://asciinema.org/a/353518.svg" width="500">
</p></a>

## Features

* **Transparent payout** of Github project contributors with every push you make to your master branch
* Minimal changes of your Github project shown in the [`seleryexample`](https://github.com/protontypes/seleryexample) to adapt OpenSelery with just a view steps.
* Detailed [`transaction history`](https://github.com/protontypes/openselery/wiki/Transaction-History) regenerated with every run of OpenSelery in your Github Wiki.
* **User defined payout configuration** by the [`selery.yml`](https://github.com/protontypes/openselery/blob/master/selery.yml).
* Dependency scanning for most languages to **even include developers of your dependencies** by the [`Libraries.io`](https://libraries.io/).
* Distribution of money is done via Coinbase. Further payment methods like Paypal or Uphold will soon been supported.
* Investors can see transparent payout logs in the [`public Github Action`](https://github.com/protontypes/openselery/actions?query=workflow%3Aopenselery).
* Self generated [`QR code`](https://raw.githubusercontent.com/wiki/protontypes/openselery/openselery/wallet_qrcode.png) for secure investment into your project host in the Wiki of your project. Wallet address is been double checked against the configured Coinbase wallet and address shown in the README badge.
* Automated user information about deposited funding transmitted to the Github user email address including a note.
* Simple simulation on your project to investigate distribution on past git history without the Coinbase tokens.


## Github Integration

Use the [template](https://github.com/protontypes/seleryexample) to integrate OpenSelery into any Github project.
*Running OpenSelery with Github Action is the most simple way for newcomer and people without a Linux shell.*



## Command Line Usage

### Run with Docker

1. Install [docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04):
```bash
cd ~
git clone https://github.com/protontypes/openselery.git
cd openselery
./build.sh
```
2. Create a token file for your user, where you store API keys and secrets:

```bash
mkdir -p ~/.openselery/secrets ~/.openselery/results
touch ~/.openselery/secrets/tokens.env
```

3. OpenSelery just needs API tokens from [Github](https://github.com/settings/tokens) when `simulation = True` and `include_dependencies = False` in your `selery.yml`. The scope of your Github token should not include additional permission than default minimal scope. Find our more about how to create Github tokens [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). Fill the Coinbase and [Libraries.io](https://libraries.io/api) tokens with XXXXX to just get started without creating an actual accounts for this APIs. 


4. Make the token file read only:
```
chmod 400 ~/.openselery/secrets/tokens.env
```

5. Clone your target repository:
```bash
git clone <target_repository>
```
6. Copy a [selery.yml](https://github.com/protontypes/seleryexample) into your <target_repository>.  Set `simulation: False` in your selery.yml to enable payouts with OpenSelery.
7. Adjust and test different configuration in simulation mode on your repository project.
8. Create a dedicated Coinbase account with limited amounts. Coinbase does not support sending email to yourself thats why you should use a dedicated email address when you are owner of the coinbase account and contributor of the project. Otherwise OpenSelery will skip this payouts.
9. Buy some cryptocurrency. See the [price list](https://help.coinbase.com/en/coinbase/trading-and-funding/pricing-and-fees/fees.html) for transferring money into the coinbase account.
10. Configure the [access control settings](https://github.com/protontypes/openselery/wiki/Coinbase-Settings) of the automated Coinbase wallet.  
11. Never transfer or store large values with automated cryptocurrency wallets. Use [recurring automated buys](https://blog.coinbase.com/easier-recurring-buys-and-sells-on-coinbase-9a3cd7ea934e) to recharge you wallet on a regular base to avoid financial and security risks. Coinbase does not charge for transferring cryptocurrency from one Coinbase wallet to another.
12. Add your coinbase API keys and secrets to the newly created file (`~/.openselery/tokens.env`). **Never store these tokens in a public repository**.

```bash
COINBASE_TOKEN=<your_coinbase_token>
COINBASE_SECRET=<your_coinbase_secret>
GITHUB_TOKEN=<your_github_tokens>
LIBRARIES_API_KEY=<your_libaries_io_tokens>
```
13. Send cryptocurrency to weighted random product contributors with a valid visible email address on GitHub:

```bash
env $(cat ~/.openselery/secrets/tokens.env) ./run.sh <target_repository>
```

#### Run directly on your host machine

1. Install the dependencies on your machine.

```bash
sudo apt update && sudo apt install git ruby ruby-dev curl python3-pip
python3 setup.py install --user
```

2. Ensure that `$HOME/.local/bin` is in `$PATH`. Check the output of `echo $PATH`. If it does not contain `.local/bin` add the following line to your dotfile for example `~/.bashrc`.

```bash
export PATH=$HOME/.local/bin:$PATH
```

3. Run OpenSelery on your target project.

```bash
env $(cat ~/.openselery/secrets/tokens.env) selery run -d ~/<target_repository> -r ~/.openselery/results/
```


## API Integrations

OpenSelery is going to supports multiple APIs and assets in the near future:
- [x] Github
- [x] Libraries.io
- [ ] Gitlab
- [x] Coinbase
- [ ] Paypal (Already tested but requires a business account activation [#34](https://developer.paypal.com/docs/api/overview/#))
- [ ] Uphold



## Support OpenSelery

### Donations

Certainly we are funded by OpenSelery over direct donations via our [`QR code`](https://raw.githubusercontent.com/wiki/protontypes/openselery/openselery/wallet_qrcode.png) . The usage and development of OpenSelery will always be free and without any charges. If you want to support us by using OpenSelery you need to add us to the [`tooling_repos.yml`](https://github.com/protontypes/seleryexample/blob/master/selery.yml).

### Contributions

Contributors on the master branch will get emails with cryptocurrency from Coinbase. Only git profiles with emails on the Github profile page are considered.
Find out more in the [Contribution Guide](https://github.com/protontypes/openselery/wiki/Contribution-Guide).

## Contact and Feedback
For further information please contact `team_at_protontypes.eu` or check out our [Wiki](https://github.com/protontypes/openselery/wiki)

<p align="center">
  <img src="docs/selery_workflow.png" width="500">
</p>


*Artwork by Miriam Winter and [undraw](https://undraw.co/)*
