# EpochMediaEngine

MPL-2.0 permits commercial use, including proprietary larger works subject to its covered-file obligations. See [Commercial use and giving back](#commercial-use-and-giving-back) for licensing, origin links and voluntary credit requests.

C++23 media timeline metadata and presentation geometry, with an optional
interactive EpochGui demonstration. The core `Epoch::MediaEngine` target owns
`media.timeline_preview`: metadata admission, revision ordering, transport,
pixel aspect, rotation and contain-fit geometry. It does not decode video or
claim audio/video synchronization.

## Source distribution

EpochGui accompanies the Media demonstration as a separate public dependency;
it remains GUI-only. The pure metadata target does not acquire GUI, Platform or
Audio dependencies. `dependencies.json` records the reviewed source graph.
No configuration fetches from the network or falls back to Engine source.

The optional demonstration reuses EpochGui_Demo's real renderer/native host.
Its Libraries page advances generated timeline metadata, draws the admitted
aspect-fit rectangle and GUI playhead. The media-only composition requires no
Audio or Platform dependency and introduces no duplicate renderer.

Configure core/tests with `cmake -S . -B build` and a module-capable generator,
then build and run CTest. To build the interactive demonstration, additionally
set `EPOCHMEDIA_BUILD_GUI_DEMO=ON`, `EPOCHGUI_DEMO_ROOT`, `EPOCHGUI_ROOT`,
and `EPOCH_MEDIA_ROOT` to the explicit
local repositories (the last points here). Build `epoch_gui_demo_app`; the
result is named `EpochMediaDemo` and opens its Libraries page. This is a source
composition, not a packaged release or runtime-acceptance claim.

The original repository history is retained. First-party source, including the
owner-authorized migrated implementation, is MPL-2.0. Historical release licenses
remain unchanged. Current source version is 0.1.0; no release artifacts or native runtime acceptance are claimed.

Reviewed EpochGui source dependency: `f83b2f15385598b8efbb028a6f391ca637e07634` (0.90.0).
Reviewed Demo source dependency: `a01214e3666ef7fc657c270d9cbd208de50064bc` (0.6.0).
All ten Windows Demo composition/configuration builds and CPU contracts pass.
The Media-owned optional composition check and native runtime acceptance remain
separate; this source graph is not a binary-release acceptance claim.

## Commercial use and giving back

Quick guide to [MPL-2.0](LICENSE); the full license governs. "Covered files"
means this library's MPL source, your changes to it, and new files containing
its code. Separate files in a larger application can use another license.

### Allowed

- [x] Use the library commercially, including in proprietary applications.
- [x] Sell applications or redistribute the library itself, changed or unchanged.
- [x] Make private/internal changes without publishing them or sending a PR.
- [x] License your separate application files under your own terms while meeting
  MPL obligations for the covered files.

### Required when distributing outside your organization

- [ ] Keep covered source, including your modifications, available under MPL-2.0.
- [ ] When shipping binaries, tell recipients how to obtain that covered source
  reasonably and promptly, charging no more than its distribution cost.
- [ ] Tell recipients the source is MPL-2.0 and include the license or explain
  how to obtain it.
- [ ] Preserve required copyright, patent, license and warranty/liability notices.
- [ ] Keep recipients' MPL source rights intact under any additional terms.

### Not allowed

- [ ] Do not make distributed covered source proprietary-only or withhold the
  covered source required for your binaries.
- [ ] Do not remove substantive required notices or present someone else's work
  as your own.
- [ ] Do not assume MPL grants rights to project names/logos or imply official
  endorsement. Use distinct product branding; see [TRADEMARKS.md](TRADEMARKS.md).

### Recommended, entirely optional

- [ ] Make the library's origin and [source repository](https://github.com/Autodidac/EpochMediaEngine) easy for
  other developers to find in dependency metadata, credits, notices or technical
  documentation. No particular README or About-screen placement is requested.
- [ ] If you credit comparable libraries or tools, include this library alongside
  them instead of obscuring its role. A factual link to
  [EpochEngine](https://github.com/Autodidac/EpochEngine) also helps support the work.
- [ ] Explain your own additions accurately. A wrapper, new name or small feature
  does not make the underlying library your original invention.
- [ ] Share useful fixes, features, tests and documentation through a
  [pull request](https://github.com/Autodidac/EpochMediaEngine/pulls); accepted contributions receive author credit.
- [ ] Follow [CONTRIBUTING.md](CONTRIBUTING.md) when choosing to contribute.

**MPL does not require an upstream pull request. But it would be a lot cooler if
you shared!** Contributions help these libraries support themselves and continued
work on EpochEngine. These recommendations add no copyright-license conditions.

See [Mozilla's MPL FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) for examples.

## License

First-party source uses **MPL-2.0**; LICENSE contains the unmodified full text.
Private modification is allowed; distribution obligations apply to covered
files under that license. Commercial use is allowed. Required notices and
third-party licenses remain in force. Historical grants are not revoked.
See NOTICE for origin, TRADEMARKS.md for separate branding rules, and
CONTRIBUTING.md / CONTRIBUTOR_LICENSE.md for explicit contribution acceptance.
