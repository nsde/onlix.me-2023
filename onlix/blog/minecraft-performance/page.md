---
tags: minecraft, performance
category: gaming
subtitle: What is fastest Minecraft 1.19.3 mod-pack?
---

The screenshot was taken with Complementary Reimagined 1.3.2.

# Best Minecraft 1.19.3 Performance Mod-Pack
All of these tests were measured on [my PC](/pc), so your results will vary.

My display resolution is 3440x1440, with an aspect ratio of 21:9.

<table>
    <thead>
        <tr>
            <th>Software</th>
            <th>Version</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>JDK Lite</td>
            <td>19.0.1</td>
        </tr>
        <tr>
            <td>Windows</td>
            <td>10 Home 22H2</td>
        </tr>
        <tr>
            <td>Prism Launcher</td>
            <td>5.1</td>
        </tr>
    </tbody>
</table>

## Disclaimer
I'm a contributor at *Fabulously Optimized*, but I'll still provide you with the most accurate and honest results I can.
Thanks to the developers of all these mod-packs for their hard work! Go check them out and support them.

## Benchmark 1 (mod-pack default settings)
All of these mod-packs:

- Are available on Modrinth
- Run on 1.19.3

As I like to keep my Minecraft version up-to-date for the most recent features and bugfixes, I some of the mod-packs were tested in their alpha version. But - as I'm writing this (1/15/22), 1.19.3 has been around for more than a month.

Everything is on default settings, except for the following:
- Seed: 1
- VSync: off
- Game mode: creative
- Java version set (see above)
- Memory allocation: Minimum 4280 MiB / Maximum 6096 MiB

**Please not that benchmark 1 isn't 100% fair since some of the mod-packs use different default settings!**

The FPS are measured after ~10 seconds of loading into the seed.

The startup time is measured from the moment I click "Launch" to the moment I can use the menu buttons.

<table>
    <thead>
        <tr>
            <th>Mod Pack</th>
            <th>Version</th>
            <th>Modloader</th>
            <th>Startup time</th>
            <th>World creation time</th>
            <th>FPS</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Fabulously Optimized</td>
            <td>4.6.0-beta.3</td>
            <td>Fabric</td>
            <td>26s</td>
            <td>12s</td>
            <td>1420</td>
            <td>Vanilla-ish defaults (graphics set to fancy, ...)</td>
        </tr>
        <tr>
            <td>Simply Optimized</td>
            <td>7.17 pre35</td>
            <td>Fabric</td>
            <td>24s</td>
            <td>13s</td>
            <td>2335</td>
            <td>Low defaults, heavily modded</td>
        </tr>
        <tr>
            <td>Adrenaline</td>
            <td>1.12.0</td>
            <td>Fabric</td>
            <td>25s</td>
            <td>13s</td>
            <td>2024</td>
            <td>Low defaults, saving world took ages</td>
        </tr>
        <tr>
            <td>Adrenaline</td>
            <td>1.12.0</td>
            <td>Quilt</td>
            <td>25s</td>
            <td>13s</td>
            <td>2040</td>
            <td>Low defaults, saving world took ages</td>
        </tr>
        <tr>
            <td>Chronos Client</td>
            <td>1.1.0</td>
            <td>Quilt</td>
            <td>22s</td>
            <td>12s</td>
            <td>1247</td>
            <td>High defaults, heavily modded</td>
        </tr>
    </tbody>
</table>

All of these mod-packs worked at the first try.

## Benchmark 2 (vanilla-ish settings)
For benchmark two, I will use the same mod-packs as in benchmark one, with the only difference being that I use the 100% vanilla options - which means there is a **fair contest and we're not comparing apples to oranges**. This is because in benchmark one, some of the mod-packs had completely different default settings.

The goal of *this benchmark* is to compare similar aesthetics.

### Settings
- FOV: Normal (70)

#### General
- Render Distance: 12 Chunks
- Max Shadow Distance: 6 Chunks
- Simulation Distance: 6 Chunks
- Brightness: 50%
- VSync: off

#### Quality
- Graphics: Fancy
- Clouds: ON
- Weather: Fast
- Leaves Quality: Default
- Particles: All
- Smooth Lighting: ON
- Biome Blend: 2 block(s)
- Entity Distance: 100%
- Entity Shadows: ON
- Vignette: ON
- Mipmap Levels: 4x

#### Animations
- All ON

#### Particles
- All ON

#### Render
- Single Fog: Default

Startup times were not measured, as there isn't any huge difference expected, and because I change the settings in-game.

Additionally, I used the same world for all these tests to ensure a fair contest.

<table>
    <thead>
        <tr>
            <th>Mod Pack</th>
            <th>Version</th>
            <th>Modloader</th>
            <th>World loading time*</th>
            <th>FPS</th>
            <th>Outdated mods</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Fabulously Optimized</td>
            <td>4.6.0-beta.3</td>
            <td>Fabric</td>
            <td>2.7s</td>
            <td>1485</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Simply Optimized</td>
            <td>7.17 pre35</td>
            <td>Fabric</td>
            <td>3.7s/1.9s</td>
            <td>1356</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Adrenaline</td>
            <td>1.12.0</td>
            <td>Fabric</td>
            <td>3.5s</td>
            <td>1345</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Adrenaline</td>
            <td>1.12.0</td>
            <td>Quilt</td>
            <td>2.8s/CRASH</td>
            <td>1346</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Chronos Client</td>
            <td>1.1.0</td>
            <td>Quilt</td>
            <td>4.8s/2.7s</td>
            <td>1476</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Yoru</td>
            <td>2.9.9</td>
            <td>Quilt</td>
            <td>5.7s/2.9s</td>
            <td>1156</td>
            <td>Iris</td>
            <td>Comes with resource packs, shader packs, and even a server</td>
        </tr>
        <tr>
            <td>waffle's Modpack</td>
            <td>2023.01.02</td>
            <td>Quilt</td>
            <td>4.7s/2.8s</td>
            <td>1173</td>
            <td>Iris</td>
            <td>Heavily modded, with a lot of QoL additions</td>
        </tr>
    </tbody>
</table>

\*It seems like on some mod-packs, the world has to be converted first. This is probably caused by *Starlight*, but shouldn't be a problem for most people.

## Conclusion
- **Fabulously Optimized** is a very fast and simplistic all-rounder, with a great community
- **Simply Optimized** also supports some snapshot versions, which is very useful for those who often test them
- **Adrenaline** has the lowest frametime [[source]](https://flightlessmango.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBaVl3IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--9921f49a75c0ef49d587e426cce848950e4fddee/Fabusally%20optimised?disposition=attachment), which I think is sometimes even more important than FPS
- **Chronos** has a great overall performance. It is like *Yoru* but without the QoL improvements and still doesn't have  
- **Yoru** is more like a quality of life than a simplistic performance mod-pack, but is still a great choice for newcomers. It comes with nice additions like shaders, resource packs, a minimap and even a server (which seems to be offline as I'm writing this, though)

