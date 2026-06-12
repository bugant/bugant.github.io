---
layout: default
title: "What’s your Plan B?"
---

“What's your Plan B?”. This is how a message from a friend on Signal read. Obviously we were talking about the progress of AI and how it is affecting software development and developers.

There is no doubt that with the advent of agents, [automatic programming](https://antirez.com/news/159) has become something really serious. You have now an always-on buddy ready to help and validate your implementation plans and code changes.

I personally started using OpenCode with different models (usually either Claude Opus or Chat GPT codex), and built some useful utility scripts. But I also used it to get a full implementation plan for different tasks and then get it to implement that.

My way of working with automatic programming is pretty standard: I start working with an agent whose role is to outline a plan; after some iterations there, a build agent can work on that plan’s implementation.

I usually ask the planning agent to also split the work into independent pieces of deliverable work (usually PRs). This works pretty well, and I found that to keep the building model performing well , starting a new agent session (where you ask it to read the plan and tell it what has already been done) for each of the PR is a good practice.

My impression is that, at the moment, the knowledge of the person interacting via the prompt with the agents and model is still very relevant. While the LLMs can usually get a good context of what is to be done, having a human providing technical background knowledge, and constraints is vital to obtain high quality outputs.

This is, for sure, changing the way I work. I sometimes miss the act of writing code: that is what I did for most of my life and I’m passionate about doing it. I still like to stay on top of what the agents do by carefully inspecting their outputs and suggesting changes where I see fit.

Moreover, it must also be said that providing an end to end service to customers is still something that requires human interactions: the software will solve problems for humans and understanding all the different aspects of a product and its use-cases remains the principal trait of well designed programs.

Will AI eat software development as an industry? I don't know. For sure it is radically changing it. I can imagine startups need fewer people to develop their proof of concepts and MVPs, and this will be a competitive advantage for them. But it is still required to have technical people in charge of owning the design and implementation of products and software artifacts.

I will hold on thinking about my Plan B, at least at the moment.
