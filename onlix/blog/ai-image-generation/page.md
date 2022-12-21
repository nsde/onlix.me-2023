---
tags: ai, tech
category: software
subtitle: It's not science fiction when we're talking about computers generating artwork. But can a layperson simply open a website and generate the next Mona Lisa?
---

# What's The Quickest AI Image Generation Website?
**Criteria:**
- Free
- No login required
- Website (no app, no download, etc.)
- Easy to use (no setup required)
- Fast (<5 mins per request)¹

¹ https://creator.nightcafe.studio/text-to-image-art failed here (no results after ~10 mins, some issues before)

## General Infos
<table>
    <thead>
        <tr>
            <th>Website</th>
            <th>
                <a href="https://www.craiyon.com/">Crayion</a>
            </th>
            <th>
                <a href="https://deepai.org/machine-learning-model/text2img">DeepAI</a>
            </th>
            <th>
                <a href="https://huggingface.co/spaces/dalle-mini/dalle-mini">Hugging Face</a>
            </th>
            <th>
                <a href="https://app.wombo.art/">Wombo</a>
            </th>
            <th>
                <a href="https://replicate.com/pixray/text2image">Pixray</a>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Live preview?</td>
            <td>No</td>
            <td>No</td>
            <td>No</td>
            <td>Yes</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>API?</td>
            <td>No</td>
            <td>Yes</td>
            <td>No</td>
            <td>No</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>Liberal license?</td>
            <td>Yes</td>
            <td>No</td>
            <td>Yes</td>
            <td>Yes </td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>Number of results</td>
            <td>9</td>
            <td>4</td>
            <td>9</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Overall score</td>
            <td>4/10</td>
            <td>5/10</td>
            <td>4/10</td>
            <td>7/10</td>
            <td>2/10</td>
        </tr>
    </tbody>
</table>


## Prompt: "Sunset with dogs"

<table>
    <thead>
        <tr>
            <th>Website</th>
            <th>
                <a href="https://www.craiyon.com/">Crayion</a>
            </th>
            <th>
                <a href="https://deepai.org/machine-learning-model/text2img">DeepAI</a>
            </th>
            <th>
                <a href="https://huggingface.co/spaces/dalle-mini/dalle-mini">Hugging Face</a>
            </th>
            <th>
                <a href="https://app.wombo.art/">Wombo</a>
            </th>
            <th>
                <a href="https://replicate.com/pixray/text2image">Pixray</a>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Output images (selection)</td>
            <td><img src="/$$ path $$/dogs-1.png"></td>
            <td>unclear license</td>
            <td><img src="/$$ path $$/dogs-2.png"></td>
            <td><img src="/$$ path $$/dogs-3.png"></td>
            <td><img src="/$$ path $$/dogs-4.png"></td>
        </tr>
        <tr>
            <td>Total minutes (minutes per image)</td>
            <td>0:55 (0:06)</td>
            <td>0:21 (0:05)</td>
            <td>0:48 (0:05)</td>
            <td>0:13 (0:13)</td>
            <td>3:00 (3:00)</td>
        </tr>
        <tr>
            <td>(Best) Image Rating ²</td>
            <td>5/10</td>
            <td>6/10</td>
            <td>8/10</td>
            <td>9/10</td>
            <td>2/10</td>
        </tr>
        <tr>
            <td>Note</td>
            <td>Partly unrecognizable shape of the animals</td>
            <td>Mostly unrecognizable shapes, only one picture was alright</td>
            <td>Partly stunning landscape, but unrecognizable shape of the animals</td>
            <td>Impressive quality, many settings</td>
            <td>Too abstract style (looks like a painting), many settings</td>
        </tr>
    </tbody>
</table>

## Prompt: "A robot and a human shake hands"

<table>
    <thead>
        <tr>
            <th>Website</th>
            <th>
                <a href="https://www.craiyon.com/">Crayion</a>
            </th>
            <th>
                <a href="https://deepai.org/machine-learning-model/text2img">DeepAI</a>
            </th>
            <th>
                <a href="https://huggingface.co/spaces/dalle-mini/dalle-mini">Hugging Face</a>
            </th>
            <th>
                <a href="https://app.wombo.art/">Wombo</a>
            </th>
            <th>
                <a href="https://replicate.com/pixray/text2image">Pixray</a>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Total minutes (minutes per image)</td>
            <td>0:48 (0:05)</td>
            <td>0:34 (0:05)</td>
            <td>0:50 (0:05)</td>
            <td>0:12 (0:12)</td>
            <td>2:48 (2:48)</td>
        </tr>
        <tr>
            <td>(Best) Image Rating ²</td>
            <td>3/10</td>
            <td>3/10</td>
            <td>8/10</td>
            <td>2/10</td>
            <td>1/10</td>
        </tr>
        <tr>
            <td>Note</td>
            <td>Only images of two robots shaking hands</td>
            <td>Only images of two robots shaking hands</td>
            <td>Just a single image actually showed a human arm</td>
            <td>Result shows the arms of two robots</td>
            <td>Looks like a mess</td>
        </tr>
    </tbody>
</table>

***

² If multiple results are returned, the best one is rated.

The rating is determined, among other things, by the quality and naturalism of the images. Also very relevant is how easy it is to figure out the text prompt.

## Conclusion
You're an API-developers? Give DeepAI a try.

You like abstract art (and also APIs)? You're going to have fun with Pixray. Except when you ask for actually realistic images...

But what website is actually the best one? Wombo, in my view. It is quick, has a variety of customization and styles. Even though it didn't quite get the prompt right, the quality is still impressive. The handshake image was a disappointment, though of course you can try other prompts.

## Credits
Thanks to [geralt](https://pixabay.com/users/geralt-9301/) for providing the image on Pixabay.
