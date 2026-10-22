[Skip to main content](https://www.remotion.dev/docs/idea#__docusaurus_skipToContent_fallback)

Copy page

On this page

The idea of Remotion is to give you a frame number and a blank canvas, to which you can render anything you want using [React](https://react.dev/).

This is an example React component that renders the current frame as text:

```
MyComposition.tsx
import { AbsoluteFill, useCurrentFrame } from "remotion";

export const MyComposition = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
        fontSize: 100,
        backgroundColor: "white",
      }}
    >
      The current frame is {frame}.
    </AbsoluteFill>
  );
};Copy
```

Remotion includes [components](https://www.remotion.dev/docs/components) for adding text, images, video, audio and shapes.

A video is a function of images over time. If you change content every frame, you'll end up with an animation.

## Video properties [​](https://www.remotion.dev/docs/idea\#video-properties "Direct link to Video properties")

A video has 4 properties:

- `width` and `height` in pixels.
- `durationInFrames`
- `fps`, standing for "frames per second".

You can obtain these values from the [`useVideoConfig()`](https://www.remotion.dev/docs/use-video-config) hook:

```
import {Interactive, useVideoConfig} from 'remotion';

export const MyComposition = () => {
  const {fps, durationInFrames, width, height} = useVideoConfig();

  return (
    <Interactive.Div
      style={{
        justifyContent: 'center',
        alignItems: 'center',
        fontSize: 60,
        backgroundColor: 'white',
        position: 'absolute',
        height: '100%',
        width: '100%',
      }}
    >
      This {width}x{height}px video is {durationInFrames / fps} seconds long.
    </Interactive.Div>
  );
};Copy
```

A video's first frame is `0` and its last frame is `durationInFrames - 1`.

## Compositions [​](https://www.remotion.dev/docs/idea\#compositions "Direct link to Compositions")

A composition is the combination of a React component and video metadata.

Register compositions to make a component renderable into a video and make it visible in the Remotion Studio composition list.

```
src/Root.tsx

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyComposition"
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
        component={MyComposition}
      />
      <Composition
        id="MyCompositionPortrait"
        durationInFrames={150}
        fps={30}
        width={1080}
        height={1920}
        component={MyComposition}
      />
    </>
  );
};Copy
```

- [Video properties](https://www.remotion.dev/docs/idea#video-properties)
- [Compositions](https://www.remotion.dev/docs/idea#compositions)

Remotion - CrawlChat

Assistant

Ask your questions about Remotion, and the bot will answer based on the documentation. Consult the sources for more accurate responses.

**Note: You won't be able to generate or edit videos in this chat.**

Thinking

Powered by [![CrawlChat](https://crawlchat.app/crawlchat-lockup.svg?dpl=dpl_AwaTBDtafs3b4xsct2P2juTGfHjZ)](https://crawlchat.com/?ref=powered-by-remotion)
