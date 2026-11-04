---
layout: post
title: "The Bot I Never Wrote"
---
I have a bot running in production, and I have no idea what's going on inside it. I never read its code. I didn't even *write* it. And that was the whole point.

I wanted to get a feel for what it's like to go all-in with coding agents. I then took on a challenge: get some simple application done without writing a single line of code.

With [automatic programming], the duties of a developer are shifting from writing code to steering and instructing agents. The human decides what needs to be done in terms of product specifications, ideas, and the desired architecture. Agents will do the “low-level” work.
I wanted to try this on a simple personal project. With my superb imagination I settled on creating a [Telegram bot to track gym activity](https://github.com/bugant/gym-journal-tg/): the point wasn’t to invent something new (and really useful) but to test this new methodology of software development.

The bot is a simple C program based on antirez’s [botlib], modified to store data in a PostgreSQL database instead of SQLite. It is meant to be used as a private chatbot, and it was all done in about four sessions of one hour each. As for the tooling, this was all done using [OpenCode] and an OpenCode Go subscription, which the project barely made a dent in. I made use of open-weight models like DeepSeek, GLM, Kimi K3, but also GPT-6 Luna. All of the models performed quite well, but I think that is also because the task at hand wasn't particularly difficult.

At first, I let the agent work on a [plan] to implement the Telegram bot: I explained what I wanted to achieve, and we iterated on some proposals for the UX in terms of the commands to implement, their syntax, and output.
For example, the following is a list of commands the user would type to record exercises done during a session at the gym:

```
/add bench 60x10x3      # three sets of 60kg x 10 reps        -> 3 rows
/add bench 60x10 55x8 50x6   # drop set, three distinct sets  -> 3 rows
/add bench 60x10       # single set                          -> 1 row
/add bench x10         # bodyweight single set (weight = 0)  -> 1 row
/add Bench Press 60x10 # multi-word exercise name supported   -> 1 row
```

And you can have a session summary using the /show command:

```
Session #13  (10/07/2026, open)
  bench       60x10 + 55x8 + 50x6     vol 1340
  squat       5x5 @ 100kg              vol 2500
  pull ups    3x10                     bw
3 exercises, 9 sets, total vol 3840 kg*rep
```

As soon as that was clarified, I asked it to keep the logic separate from the pure bot-related code, and it started working on it. I also worked on the ergonomics of the application's configurations: for example, I wanted to have the API key for the bot in an env variable. After that, the first version of the bot was ready for testing.

In the first implementation only unit tests were added, but when I tried it end-to-end, issues started to arise. The agent was quick to fix those once I provided the logs and a brief description of what happened.
Anyway, after the second bug, I felt it was too slow as a process, and thus asked the agent to build an end-to-end test infrastructure. It settled on using Python and, relying only on the standard library, it built a very nice and useful [testing framework](https://github.com/bugant/gym-journal-tg/tree/a3691affcfd89dfd2ac9b1f0a43df1417967b171/tests/e2e). Telegram server requests and responses were mocked and the agent added the concept of test scenarios. Each scenario is made up of different steps, each one representing a user interaction with the bot. A step also describes the expected bot response, the database queries, and their results.
I was amazed to see the agent building this fully autonomously without asking for or requiring any additional hint or information. These are the kind of activities that are quite easy and straightforward to do, but at the same time could take a person a long time to implement. Having tools that automate this type of work is extremely effective and efficient.

With that in place, the agent found and fixed all the remaining issues.

At this point all was ready for prime time. As my employer, Aiven, had recently released [Runtime], I thought it would be interesting to test it out. Moreover, Aiven also provides a [free-tier] plan for PostgreSQL, which was what I needed. I equipped the agent with a link to the documentation and it gave me the [artifacts I needed](https://github.com/bugant/gym-journal-tg/commit/9113cc3c82b93e6f5c2d419d6cf81b428a90a519) to deploy the application and have the connected database service provisioned along with it.

All in all it was quite a smooth experience: everything progressed without any major issue or blocker.
I must admit I don’t feel like I really know what’s going on inside the bot, and if that were a business-critical application, that would make me a bit nervous.
But that’s where the future of the software industry is heading. If we really want to embrace the productivity gains that automatic programming offers, then humans should very seldom be involved in [reading code](https://claude.dev/blog/solving-code-review-at-anthropic/) and, instead, focus on [deeper analysis and product decisions](https://antirez.com/news/169). Designing a proper way to test systems developed using this strategy is thus very important.
Software engineers are still the ones who are in charge of the main architecture designs and who decide whether something is worth doing or not.

---

*Disclaimer: I am an Aiven employee, and this post mentions Aiven products. Everything written here reflects my personal experience and opinions only, not those of my employer.*


[automatic programming]: https://antirez.com/news/159
[botlib]: https://github.com/antirez/botlib
[plan]: https://github.com/bugant/gym-journal-tg/blob/a3691affcfd89dfd2ac9b1f0a43df1417967b171/GYM-JOURNAL-PLAN.md
[Runtime]: https://aiven.io/runtime
[free-tier]: https://aiven.io/free-tier
[OpenCode]: https://opencode.ai
