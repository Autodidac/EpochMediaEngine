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
Other working dependency identities remain pending; this is not a release-ready graph.

## Commercial use and giving back

A larger combined work may use its own license, including a proprietary commercial license, provided the covered files remain under MPL-2.0 and its applicable obligations are met.

Commercial use and standalone commercial redistribution are allowed by MPL-2.0;
you do not have to combine EpochMediaEngine with another product. When distributing
covered source modifications, make the covered modified files available under
MPL-2.0 and retain its required notices. Follow LICENSE for the precise source
availability and executable distribution obligations. Private edits do not
require publication, and MPL does not require an upstream pull request.

Please give visible, accurate credit in your application's About screen or its
README, linking to [the canonical EpochMediaEngine repository](https://github.com/Autodidac/EpochMediaEngine)
and [EpochEngine](https://github.com/Autodidac/EpochEngine), which this work
supports. Please offer generally useful changes as upstream pull requests with
clear author credit and provenance, following CONTRIBUTING.md. These are
community requests, not additional copyright-license conditions.
Accepted pull-request contributions retain author credit in GitHub history and in project acknowledgements where applicable.


Keep derivative product branding distinct and do not imply ownership of another
author's work or official endorsement. Factual origin, contributor credit and API
compatibility references are welcome; see TRADEMARKS.md.

## License

First-party source uses **MPL-2.0**; LICENSE contains the unmodified full text.
Private modification is allowed; distribution obligations apply to covered
files under that license. Commercial use is allowed. Required notices and
third-party licenses remain in force. Historical grants are not revoked.
See NOTICE for origin, TRADEMARKS.md for separate branding rules, and
CONTRIBUTING.md / CONTRIBUTOR_LICENSE.md for explicit contribution acceptance.
