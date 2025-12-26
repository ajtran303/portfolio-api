# Case Study: Haunted House Tycoon

A deterministic park management simulation built with React, TypeScript, Phaser, and Zustand.

## Overview

**Haunted House Tycoon** is a single-player management game where players build and operate a haunted theme park. Visitors pay to be scared, but push them too hard and they die. The challenge is balancing fear (revenue) against survival (sustained income).

**Tech Stack:** Vite, React, TypeScript, Phaser 3, Zustand, Vitest

**Timeline:** Ongoing solo project

**Role:** Design, Architecture, Implementation

---

## The Challenge

Build a simulation game that is:

1. **Deterministic** - Same inputs always produce same outputs
2. **Testable** - Core logic decoupled from rendering
3. **Readable** - Player understands why they succeed or fail
4. **Emergent** - Simple rules create complex outcomes

Most simulation games hide complexity behind randomness. I wanted failure to feel _earned_ - traceable to player decisions, not dice rolls.

---

## Architecture

### Three-Layer Design

1. UI Layer (React + Phaser)
   - Renders state, dispatches actions
2. Runtime Layer (Zustand)
   - Single source of truth, tick loop
3. Core Layer (Pure Functions)
   - No side effects, fully testable

**Why this matters:**

- Core game logic has zero dependencies on React or Phaser
- Unit tests run in milliseconds without rendering
- Same logic could power a different frontend (terminal, canvas, WebGL)
- Determinism is guaranteed by construction

### The Two-Grid System

The park uses a hub-and-spoke model:

- **Midway** - Central grid where visitors spawn, recover, and exit
- **Attractions** - Isolated sub-grids connected via portal tiles

Visitors physically transition between grids through portals, creating natural choke points and flow management challenges.

`type VisitorLocation = { type: 'midway' } | { type: 'attraction'; attractionId: string };`

This separation enables:

- Different rules per zone (fear recovers on midway, not in attractions)
- Visible queues at transition points
- Isolated failure cascades (one attraction failing doesn't instantly kill the park)

---

## Key Technical Decisions

### Deterministic Simulation

Every game tick processes systems in a fixed order:

1. Spawn visitors
2. Apply intent rules
3. Move visitors
4. Apply room effects
5. Decay emotions
6. Check exits
7. Calculate economy
8. Check failure

No `Math.random()`. Visitors processed by ID order. Same seed, same run.

**Result:** Save/load is trivial. Bug reports are reproducible. Tests are reliable.

### Pure Function Architecture

All core logic is implemented as pure functions.

**Result:**

- Functions are trivially testable
- No hidden state mutations
- Easy to reason about data flow

### Blocking States for Spatial Constraints

When visitors can't move (congestion, blocked paths), they enter internal blocking states:

- `queued-to-enter` - Waiting at portal, attraction entry blocked
- `queued-to-return` - At attraction exit, midway return blocked
- `trapped` - No path to exit exists

These are _spatial_ states, not _intent_ states. A visitor can want to exit (`intent: 'exit'`) while being physically stuck (`blockingState: 'trapped'`).

**Result:** Visible queues, emergent congestion, cascading failures from poor layout.

---

## Game Design Integration

### Fear as a Resource

Most games treat negative emotions as purely bad. Here, fear is _money_:

- Low fear → low spending
- High fear → high spending (fear bonus)
- Too much fear → panic death

Players must push visitors close to the edge without going over. This creates tension without randomness.

### Death as Information

When visitors die, it's diagnostic:

**Panic** Too much fear - reduce scare rooms or add recovery
**Misery** Flow problem - congestion, no amenities, stuck visitors

The game is cruel but never opaque. Players can always trace what went wrong.

### Staff as Risk Amplifiers

Staff don't make the park safer - they make it _scarier_:

- Each staff member amplifies fear in scare rooms
- More fear = more money = more deaths
- Staff have ongoing upkeep costs

This inverts the typical "hire more staff = better" pattern. Overstaffing is a trap.

---

## Testing Strategy

### Shared Test Factories

Example: adding a new field to `Visitor` requires updating one factory, not hundreds of tests.

### Behavior-Driven Tests

Tests describe behavior, not implementation details.

---

## Documentation as Design Tool

The project includes living documentation:

- **BALANCE.md** - All tunable constants with rationale
- **GAME_DESIGN.md** - Design philosophy, intended experience
- **CONTRIBUTING.md** - How to add features with examples

Documentation is updated alongside code, not after.

---

## Results & Learnings

### What Worked

- **Pure functions** made the codebase dramatically easier to test and debug
- **Determinism** eliminated an entire class of bugs (race conditions, random failures)
- **Two-grid system** created emergent gameplay without complex AI
- **Blocking states** made invisible problems (congestion) visible

### What I'd Do Differently

- **Earlier balance testing** - Some constants need playtesting to tune properly
- **Visual feedback first** - Good feedback systems should be designed alongside mechanics, not added later

### Technical Metrics

- Core logic: ~3,000 lines of pure TypeScript
- Test coverage: All core systems have unit tests
- Zero external dependencies in core layer
- Sub-10-seconds test suite execution

---

## Future Roadmap

**Next: Hardcore Mode (Tombstones)**

- Deaths leave permanent obstacles
- Attractions can become "grinders" (visitors enter, can't exit)
- Optional toggle for difficulty preference

**Later:**

- Visitor archetypes (thrill seekers, easily scared)
- Scenario challenges
- Cloud save with deterministic replay

---

## Links

<!-- - [Play the Game](#) *(placeholder)* -->

- [GitHub Repository](https://github.com/ajtran303/haunted-house-tycoon/)
<!-- - [Game Design Document](./GAME_DESIGN.md) -->

<!-- --- -->
<!--
## Screenshots

*(Add screenshots here)*

- Main gameplay view showing midway and visitor flow
- Attraction builder with scare rooms
- HUD displaying economy and visitor stats
- Failure screen with diagnostic summary -->
