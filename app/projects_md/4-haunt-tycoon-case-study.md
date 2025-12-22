# Case Study: Haunted House Tycoon

## Summary

Haunted House Tycoon is a management simulation designed with **system trustworthiness as a primary engineering constraint**. Rather than prioritizing early content or polish, the project focuses on deterministic state transitions, explicit lifecycle control, and failure reporting derived from real system state. All uncertainty arises from player decisions rather than hidden or uncontrolled simulation behavior.

**Status**: Ongoing project focused on strengthening and validating core system guarantees.

[View the code on GitHub](https://github.com/ajtran303/haunted-house-tycoon/)

[Track dev progress on Trello](https://trello.com/b/KlfRz1Fa/haunt-tycoon)

---

## Problem

Many simulation and tycoon games lose player trust due to:

- nondeterministic updates  
- hidden simulation during pause or load  
- unclear failure causes  
- unsafe restarts or corrupted saves  

These issues are often discovered late, when they are expensive and difficult to fix.

This project addresses those risks early by treating **correctness, determinism, and explainability as first-class design constraints**.

---

## Design Approach

Development is structured into strict phases, each with a non-negotiable promise:

- **MVP**  
  A deterministic simulation that runs and can be lost, with no saves or explanation layers.

- **Alpha**  
  Clear cause-and-effect visibility, explicit lifecycle states (`running`, `paused`, `failed`), and restarts that never leak state.

- **Beta**  
  Deterministic save/load behavior, no hidden simulation during pause or load, and failure explanations grounded in real system metrics.

Content expansion is deferred until these guarantees are proven.

---

## Key Technical Decisions

- **Deterministic Simulation Kernel**  
  All logic updates through a single authoritative tick loop; identical inputs always produce identical outcomes.

- **Explicit Lifecycle Control**  
  Simulation, UI, and time flow are gated behind lifecycle state; no mutation occurs unless the game is explicitly running.

- **Exact Save/Load Rehydration**  
  Saves serialize authoritative state only; loads restore identical state and resume solely through explicit player action.

- **Honest Failure Explanation**  
  Failure summaries are derived directly from real simulation metrics, with no fabricated warnings.

---

## Outcome

The result is a game where simulation behavior is provable rather than assumed, restarts and resumes are always safe, and failure feels fair because it is explainable. Although a game project, the architecture reflects **production-grade systems design** with clear invariants, strict boundaries, and measurable correctness.

---

## Key Takeaway

**Haunt Tycoon is not about shipping features quickly — it is about proving a system can be trusted before asking players to invest their time.**
