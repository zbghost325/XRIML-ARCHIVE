---
title: "Meta Quest Link - Login & Setup Flow — Prepare the PC - Fix, Runtime & Codec"
description: "Do these before opening Meta Horizon Link: run the fix, set the VR runtime, then switch the Link video codec to H.265 in the Oculus Debug Tool. No admin rights needed."
template: document.html
category: "Troubleshooting"
pages: 1
stylesheet: style.css
source: "codec-fix.html"
tags:
  - "Unity"
  - "Quest 3"
  - "Link"
hide:
  - navigation
  - toc
---
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
