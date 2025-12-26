# Case Study: Haunted House Tycoon

A deterministic park management simulation built with React, TypeScript, Phaser, and Zustand.

## Overview

**Haunted House Tycoon** is a single-player management game where players build and operate a haunted theme park. Visitors pay to be scared, but push them too hard and they die. The challenge is balancing fear (revenue) against survival (sustained income).

**Tech Stack:** Vite, React, TypeScript, Phaser 3, Zustand, Jest, Tailwind CSS

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

1. **UI Layer** (React + Phaser) - Renders state, dispatches actions
2. **Runtime Layer** (Zustand) - Single source of truth, tick loop
3. **Core Layer** (Pure Functions) - No side effects, fully testable

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

Location is tracked as: `{ type: 'midway' }` or `{ type: 'attraction', attractionId: string }`

This separation enables:

- Different rules per zone (fear recovers on midway, not in attractions)
- Visible queues at transition points
- Isolated failure cascades (one attraction failing doesn't instantly kill the park)

---

## Key Technical Decisions

### Deterministic Simulation

Every game tick processes systems in a fixed order:

1. Advance time (tick/day)
2. Check structural blocks (entrance/exit blocked → fail)
3. Spawn visitors at entrance
4. Apply intent rules (explore → exit after N ticks)
5. Move visitors (multi-grid with portal transitions)
6. Calculate amenity purchases
7. Apply room emotion effects (on entry)
8. Decay happiness (midway only)
9. Recover fear (midway only)
10. Remove emotional exits (panic/misery deaths)
11. Calculate spending
12. Deduct upkeep
13. Despawn at exit
14. Check bankruptcy

No `Math.random()`. Visitors processed by ID order. Same seed, same run.

**Result:** Save/load is trivial. Bug reports are reproducible. Tests are reliable.

### Pure Function Architecture

All core logic is implemented as pure functions.

Example - emotion application returns a new visitor object:

`applyEmotionDelta(visitor, { fear: 10 })` → new visitor with clamped fear

**Result:**

- Functions are trivially testable
- No hidden state mutations
- Easy to reason about data flow

### Blocking States for Spatial Constraints

When visitors can't move (congestion, blocked paths), they enter internal blocking states:

- **queued-to-enter** - On portal tile, attraction entry occupied
- **queued-to-return** - At attraction exit, midway return blocked
- **trapped** - Inside attraction, no valid moves

These are _spatial_ states, not _intent_ states. A visitor can want to exit (`intent: 'exit'`) while being physically stuck (`blockingState: 'trapped'`).

**Result:** Visible queues, emergent congestion, cascading failures from poor layout.

### Seeded Pseudo-Random Movement

Visitors need to move differently without true randomness.

Direction selection uses: `hash32(visitorId * 1000003 + tickBucket) % 4`

Each visitor gets a deterministic but varied movement pattern. Same visitor, same tick, same direction - but different visitors move differently.

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

- **Panic** - Too much fear. Reduce scare rooms, add recovery time.
- **Misery** - Happiness depleted. Add amenities, reduce congestion.

The game is cruel but never opaque. Players can always trace what went wrong.

Deaths are tracked cumulatively in the UI, unlocking visibility only after the first death of each type occurs.

### Staff as Risk Amplifiers (Planned)

Staff don't make the park safer - they make it _scarier_:

- Each staff member amplifies fear in scare rooms
- More fear = more money = more deaths
- Staff have ongoing upkeep costs
- Diminishing returns prevent linear scaling

This inverts the typical "hire more staff = better" pattern. Overstaffing is a trap.

---

## Dev Mode

Development tools are gated behind a `DEV_MODE` flag:

**Dev Panel:**

- Cheat buttons (+$1000, spawn visitors, clear park)
- Quick setup (auto entry/exit, template haunts)
- Debug toggles (visitor intent labels)

**Console Access:**

- `__gameState()` - Full store inspection
- `__tick()` - Manual tick advancement (works while paused)
- `__bootScene` - Phaser scene access

**Additional:**

- 10x speed option
- Scared visitor count in fear bar

Dev features stay in dev code, keeping game state clean.

---

## Testing Strategy

### Shared Test Factories

`makeVisitor({ fear: 50 })` returns a complete Visitor with defaults plus overrides.

Adding a new field to `Visitor` requires updating one factory, not hundreds of tests.

### Behavior-Driven Tests

Tests describe behavior, not implementation:

"converts explore to exit after threshold ticks" - create visitor with `intent: 'explore'`, apply rules at tick 31, expect `intent: 'exit'`

---

## Documentation as Design Tool

The project includes living documentation:

- **BALANCE.md** - All tunable constants with rationale
- **GAME_DESIGN.md** - Design philosophy, intended experience
- **CONTRIBUTING.md** - How to add features with examples
- **MOVEMENT.md** - Visitor movement system deep dive
- **STAFF.md** - Staff feature specification
- **DEMOLITION.md** - Room demolition specification

Documentation is updated alongside code, not after. Feature specs are written before implementation.

---

## Results & Learnings

### What Worked

- **Pure functions** made the codebase dramatically easier to test and debug
- **Determinism** eliminated an entire class of bugs (race conditions, random failures)
- **Two-grid system** created emergent gameplay without complex AI
- **Blocking states** made invisible problems (congestion) visible
- **Dev mode** accelerated iteration without polluting game state

### What I'd Do Differently

- **Earlier balance testing** - Some constants need playtesting to tune properly
- **Visual feedback first** - Good feedback systems should be designed alongside mechanics, not added later
- **Feature specs upfront** - Writing STAFF.md and DEMOLITION.md before coding clarified scope significantly

### Technical Metrics

- Core logic: ~4,000 lines of pure TypeScript
- Test coverage: All core systems have unit tests
- Zero external dependencies in core layer
- Sub-10-second full test suite execution

---

## Current Status & Roadmap

**Current: Alpha**

- Core loop complete
- Two-grid system with portals
- Visitor emotions and spending
- Amenities
- Dev tooling
- Death tracking

**Next: Beta**

- Staff system (fear amplifiers)
- Room demolition
- Save/load
- Tutorial

**Future: Post-Beta**

- Game modes (Normal vs Hardcore)
- Visitor archetypes (thrill seekers, easily scared)
- Day/night cycle
- Scenario challenges
- Cloud save with deterministic replay

---

## Links

- [GitHub Repository](https://github.com/ajtran303/haunted-house-tycoon/)
