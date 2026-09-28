---
title: "Meta Quest Link - Login & Setup Flow"
description: "Double-sided sheet for getting Quest Link working on lab PCs. Page 1: run the fix, set the VR runtime and switch the Link codec to H.265. Page 2: enable the Link settings, connect, and troubleshoot."
template: document.html
category: "Troubleshooting"
pages: 2
stylesheet: style.css
source: "quest-link-codec-fix.html"
tags:
  - "Unity"
  - "Quest 3"
  - "Link"
hide:
  - navigation
  - toc
---
<div class="xg-part xg-part-1" id="page-1">
<div class="sheet">
    <div class="titlebar"><h1 id="meta-quest-link-login-setup-flow">Meta Quest Link - Login &amp; Setup Flow</h1><p class="sub">Prepare the PC - Fix, Runtime &amp; Codec</p></div>
    <div class="body">
      <p class="intro">
        Do these <b>before opening Meta Horizon Link</b>: run the fix, set the VR runtime, then switch the
        Link video codec to <b>H.265</b> in the Oculus Debug Tool. No admin rights needed.
      </p>

      <!-- STEPS 1 + 2 -->
      <div class="step step1">
        <div class="s2main" style="grid-template-columns:1fr 1.6fr;align-items:center;">
          <div>
            <div class="step-head"><div class="num">1</div>
              <div class="step-title">Run the fix<span>Desktop shortcut</span></div></div>
            <figure class="iconfig">
              <img src="images/img-001.jpg" alt="">
              <figcaption><b>fix_oculus_OVR88948175</b><br>grey gears icon</figcaption>
            </figure>
          </div>
          <div>
            <div class="step-head"><div class="num">2</div>
              <div class="step-title">Set the VR runtime<span>FileWave Kiosk</span></div></div>
            <figure class="sdfig">
              <img src="images/img-002.jpg" alt="">
              <figcaption>Click <b>Install</b> on <b>Set VR Runtime to OpenXR/Oculus</b> - or the <b>SteamVR</b> script if that is your target.</figcaption>
            </figure>
          </div>
        </div>
      </div>

      <hr class="sep">

      <!-- STEP 3: debug tool / codec -->
      <div class="step step1">
        <div class="step-head"><div class="num">3</div>
          <div class="step-title">Update the debugger settings<span>Oculus Debug Tool</span></div></div>

        <p class="substep">Find OculusDebugTool.exe - quit Meta Quest Link first</p>
        <div class="navstrip">
          <figure><span class="badge">1</span><img src="images/img-003.jpg" alt=""><figcaption>In <b>Local Disk (C:)</b>, open <b>Program Files</b></figcaption></figure>
          <figure><span class="badge">2</span><img src="images/img-004.jpg" alt=""><figcaption>Open <b>Oculus</b> (or <b>Meta Horizon</b>), then <b>Support</b></figcaption></figure>
          <figure><span class="badge">3</span><img src="images/img-005.jpg" alt=""><figcaption>In <b>Support</b>, open <b>oculus-diagnostics</b></figcaption></figure>
          <figure><span class="badge">4</span><img src="images/img-006.jpg" alt=""><figcaption>Double-click <b>OculusDebugTool</b></figcaption></figure>
        </div>

        <p class="substep">Change two settings - under the "Oculus Link" section</p>
        <div class="s2main" style="grid-template-columns:1.35fr 1fr;align-items:start;">
          <div style="display:flex;flex-direction:column;gap:10px;">
            <figure class="setfig"><span class="badge">5</span><img src="images/img-007.png" alt=""><figcaption>Set <b>Video Codec</b> to <span class="v">H.265</span></figcaption></figure>
            <figure class="setfig"><span class="badge">6</span><img src="images/img-008.png" alt=""><figcaption>Set <b>Sliced Encoding</b> to <span class="v">Off</span></figcaption></figure>
            <p class="note" style="margin:0;">Leave every other value as-is, then close the tool.</p>
          </div>
          <figure class="dtwin" style="margin:0;">
            <img src="images/img-009.jpg" alt="">
            <figcaption class="cap" style="text-align:center;font-size:10px;color:var(--muted);margin-top:4px;">Both rows sit together under the <b>Oculus Link</b> section.</figcaption>
          </figure>
        </div>
      </div>

      <div class="tips">
        <div><h3 id="good-to-know">Good to know</h3><p>A <b>standard (non-admin) user</b> can make the codec change. The setting is <b>per user</b> on the <b>XRIML</b> or <b>RY324</b> PC. You should only need to do this <b>once for your user</b>, but it never hurts to re-check if the issue appears again.</p></div>
        <div><h3 id="what-to-expect">What to expect</h3><p>This workaround is for <b>graphical issues</b> in the headset caused by <b>GPU driver errors</b>. The connection can be unstable at first, then settles - very little tearing, and no major artifacting.</p></div>
      </div>

      <div class="foot"><span>Meta Quest Link - prepare the PC (steps 1-3)</span><span>Page 1 of 2</span></div>
    </div>
  </div>
</div>
<div class="xg-part xg-part-2" id="page-2">
<div class="sheet">
    <div class="titlebar"><h1 id="meta-quest-link-login-setup-flow-2">Meta Quest Link - Login &amp; Setup Flow</h1><p class="sub">Connect over Link - Settings &amp; Troubleshooting</p></div>
    <div class="body">
      <p class="intro">
        With the PC prepared (page 1), open <b>Meta Horizon Link</b>, turn on the settings below, then connect.
        If the PC and headset can't find each other, see the <b>troubleshooting</b> at the bottom.
      </p>

      <!-- STEP 4 -->
      <div class="step step1">
        <div class="step-head"><div class="num">4</div>
          <div class="step-title">Open Meta Horizon Link &amp; sign in<span>Desktop app</span></div></div>
        <p class="lead" style="margin:2px 0 0;">
          Launch the <b>Meta Horizon Link</b> desktop app and sign in. The <b>Developer</b> settings below need a
          <b>Meta developer account</b> - quick sign-up at <b>developers.meta.com/horizon/sign-up</b>.
        </p>
      </div>

      <hr class="sep">

      <!-- STEP 5 -->
      <div class="step step1">
        <div class="step-head"><div class="num">5</div>
          <div class="step-title">Enable the Link settings<span>Settings &#9656; General and Developer tabs</span></div></div>

        <p class="sublab">General tab</p>
        <figure class="sdfig" style="margin-bottom:10px;">
          <img src="images/img-010.jpg" alt="">
          <figcaption>Turn on <b>Unknown Sources</b> - lets apps that Meta has not reviewed run over Link.</figcaption>
        </figure>

        <p class="sublab">Developer tab <span style="text-transform:none;font-weight:600;">(needs a Meta developer account)</span></p>
        <div class="s2main" style="grid-template-columns:1.5fr 1fr;align-items:start;">
          <figure class="mhlfig" style="margin:0;"><img src="images/img-011.jpg" alt=""></figure>
          <div>
            <ul class="chklist">
              <li><b>Developer Runtime Features</b></li>
              <li><b>Passthrough</b> over Meta Horizon Link</li>
              <li><b>Passthrough Camera API</b> permissions</li>
              <li><b>Eye tracking</b> over Meta Horizon Link</li>
              <li><b>Spatial Data</b> over Meta Horizon Link</li>
              <li class="opt">Natural Facial Expressions <i>(optional)</i></li>
            </ul>
          </div>
        </div>
      </div>

      <hr class="sep">

      <!-- STEP 6 -->
      <div class="step step1">
        <div class="step-head"><div class="num">6</div>
          <div class="step-title">Launch &amp; connect<span>Enable Link on the headset</span></div></div>
        <div class="s2main" style="grid-template-columns:1.55fr 1fr;align-items:center;">
          <p class="lead" style="margin:0;">
            Start your app, <b>SteamVR</b>, or your dev platform. Put on the headset - when the
            <b>Enable Link</b> prompt appears, select <b>Enable</b>. No prompt? <b>Unplug and replug</b> the cable to make it reappear.
          </p>
          <figure class="hmdfig">
            <img src="images/img-012.png" alt="">
            <figcaption>The on-headset Enable Link prompt.</figcaption>
          </figure>
        </div>
      </div>

      <hr class="sep">

      <!-- Troubleshooting - last -->
      <div class="step step1">
        <div class="step-head"><div class="num" style="font-size:22px;">?</div>
          <div class="step-title">Troubleshooting<span style="text-transform:none;">If the PC and Headset can't find each other / won't connect!</span></div></div>
        <ul class="rows" style="margin-top:2px;">
          <li style="align-items:center;"><span class="tag">RE-CHECK</span><div>Confirm <b>Video Codec = H.265</b> and <b>Sliced Encoding = Off</b> in OculusDebugTool.exe (page 1).</div></li>
          <li style="align-items:center;"><span class="tag">RESTART</span><div>Restart <b>both</b> the PC and the headset - the settings are saved across restarts.</div></li>
          <li style="align-items:center;"><span class="tag">RECONNECT</span><div>Open <b>Link</b> again; the PC and headset should re-pair.</div></li>
        </ul>
      </div>

      <div class="foot"><span>Meta Quest Link - connect over Link (steps 4-6)</span><span>Page 2 of 2</span></div>
    </div>
  </div>
</div>
