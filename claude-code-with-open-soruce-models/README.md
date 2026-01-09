# Run Claude Code with Open-Source Models (Using Ollama)


Ollama supports Anthropic's API format !

https://ollama.com/blog/claude

## 🎥 [Opening – 0:00–0:30]

**[On screen: Terminal animation + code flying in]**

**Narrator:**

What if you could run **Claude Code**…
but powered by an **open-source model**…
locally on your machine?

No API bills.
No cloud dependency.
Just fast, local AI coding.

Today, I’ll show you how to run Claude Code using open-source models through **Ollama** — in just five minutes.

Let’s go.

---

## 🧠 [What’s Happening Here? – 0:30–1:00]

**Narrator:**

Here’s the cool part.

**Ollama** now supports the **Anthropic API format**.

That means tools built for Claude — like **Claude Code** — can talk to local models as if they were Anthropic’s own models.

So we’re basically:

* Running a local model
* Making it pretend to be Claude’s API
* And connecting Claude Code to it

Let’s set it up.

---

## ⚙️ Step 1 – Install Ollama (1:00–1:20)

**On screen:**

```
Download from: https://ollama.com
```

**Narrator:**

First, install **Ollama**.

It runs large language models locally on macOS, Windows, and Linux.

Once installed, make sure it’s running:

```
ollama --version
```

Good? Let’s pull a model.

---

## 🤖 Step 2 – Pull a Coding Model (1:20–1:50)

**On screen:**

```
ollama pull qwen2.5-coder
```

**Narrator:**

Now we download a coding model.

We’ll use **Qwen2.5-Coder** — a strong open-source coding model.

This may take a few minutes depending on your internet speed.

Once it’s done, your local AI coder is ready.

---

## 🛠 Step 3 – Install Claude Code (1:50–2:20)

**On screen:**

```
https://code.claude.com/docs/en/setup
```

**Narrator:**

Next, install **Claude Code** globally using npm.

This is Anthropic’s official CLI coding assistant.

Normally, it connects to Claude’s API.

But we’re about to redirect it.

---

## 🔁 Step 4 – Point Claude Code to Ollama (2:20–3:20)

**On screen:**

```
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_BASE_URL=http://localhost:11434
```

**Narrator:**

Here’s the magic.

We override two environment variables:

First:
We fake the authentication token.

Second:
We change the base URL to localhost — where Ollama runs.

Ollama now speaks the Anthropic API format.

So Claude Code thinks it’s talking to Anthropic…

But it’s actually talking to your local model.

That’s the hack.

On Windows PowerShell, use:

```
setx ANTHROPIC_AUTH_TOKEN ollama
setx ANTHROPIC_BASE_URL http://localhost:11434
```

Restart your terminal afterward.

---

## 🚀 Step 5 – Run It (3:20–4:10)

**On screen:**

```
claude --model qwen2.5-coder
```

**Narrator:**

Now launch Claude Code…

But tell it to use the model we pulled.

And that’s it.

You’re now running:

Claude Code
Powered by Qwen
Through Ollama
Fully local.

No cloud calls.

No usage tracking.

Just your machine.

---

## 🧩 What You Just Built (4:10–4:40)

**Narrator:**

You created a local AI coding stack:

Claude Code → Anthropic API format → Ollama → Open-source model

This means you can:

* Build apps offline
* Experiment without API limits
* Swap models anytime
* Customize your AI workflow

It’s flexible.
And powerful.

---

## ⚠️ Things to Keep in Mind (4:40–5:00)

**Narrator:**

A few notes:

* Performance depends on your hardware
* Bigger models need more RAM
* Responses may differ from official Claude models
* Tool support may vary

But for local development?

This setup is incredible.

---

## 🎬 Closing

**Narrator:**

And that’s it.

Five minutes.
Open-source model.
Claude Code running locally.

If you found this helpful, consider exploring other models in Ollama — and experimenting with different coding workflows.

Welcome to local AI development.

Happy building 🚀
