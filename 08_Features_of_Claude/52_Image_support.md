# 52. Image support

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287778
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Image support
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in countless ways. You can ask Claude to describe what's in an image, compare multiple images, count objects, or perform complex visual analysis tasks.

Image Handling Basics

There are several important limitations to keep in mind when working with images:

Up to 100 images across all messages in a single request
Max size of 5MB per image
When sending one image: max height/width of 8000px
When sending multiple images: max height/width of 2000px
Images can be included as base64 encoding or a URL to the image
Each image counts as tokens based on its dimensions: tokens = (width px × height px) / 750

To send an image to Claude, you include an image block in your user message alongside text blocks. Here's the structure:

with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])

Message Flow

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text block containing its analysis.

Prompting Techniques

The key to getting good results with images is applying the same prompting engineering techniques you'd use with text. Simple prompts often lead to poor results. For example, asking "How many marbles are in this image?" might return an incorrect count.

You can dramatically improve Claude's accuracy by:

Providing detailed guidelines and analysis steps
Using one-shot or multi-shot examples
Breaking down complex tasks into smaller steps

Step-by-Step Analysis

Instead of a simple question, provide Claude with a methodology:

Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?

One-Shot Examples

You can also improve accuracy by providing examples within your message. Include an image with a known count, state the correct answer, then ask about your target image. This gives Claude a reference point for the type of analysis you want.

Real-World Example: Fire Risk Assessment

Here's a practical application: automating fire risk assessments for home insurance. Instead of sending inspectors to every property, insurance companies can use satellite imagery and Claude's analysis.

The system analyzes satellite images to identify:

Dense, close-packed trees near the residence
Difficult access routes for emergency services
Branches overhanging the residence

Rather than a simple prompt like "provide a fire risk score," a well-structured prompt breaks down the analysis into specific steps:

Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:
   - The largest roofed structure
   - Typical residential features (driveway connection, regular geometry)
   - Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:
   - Identify any trees whose canopy extends directly over any portion of the roof
   - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%,

---

## 🎬 Transcript (English)

The next advanced capability of Claude that we are going to investigate is Claude's vision capabilities. Whenever we send a user message off to Claude, we can optionally include images inside of the message. We can then ask Claude to do just about anything you can possibly imagine with these images. So we could ask Claude to tell us what is contained inside them. We could ask Claude to compare different images. We can ask Claude to count different objects. Really, there's a lot of different possibilities here. The first thing I want you to understand around image handling is some of the different restrictions or requirements. We can send up to 100 images across all the messages inside of a single request. There are some limitations around the size of each image and the height and width as well. And finally, you need to understand that whenever you send an image off to Claude, that is going to count for some number of tokens that you are going to be charged for. There is an equation you can use to roughly calculate how many tokens you'll be charged for based upon the height and the width of the image in pixels. To send an image off to Claude, we are going to include yet another type of block inside of a user message. This is an image block. We can attach multiple different image blocks inside of one single user message. Each image block is going to hold a reference to a single image. Inside this image block, we can attach either the raw image data, which is what I showed in this diagram over here on the right-hand side, or alternatively, we can provide a URL to an image that is hosted somewhere online. So now that we understand some of the technical limitations here and how we send the image off, there's something really important that I want to address right away. Whenever an engineer starts making use of images with Claude, well, I notice very often they start using prompts that are very simple, even kind of like the prompt I've gotten this example right here. The number one way to get good results out of Claude when you are making use of images is to continue to have a strong focus on prompting techniques. So if you just throw an image off to Claude and then put in a very simple prompt, very often you are not going to get back a good result. For example, consider the conversation on the right-hand side. I put in an image with 12 marbles. I actually tested this by the way and I asked it very simply how many marbles are in this image. And sure enough, I got back an incorrect count of 13. We can dramatically increase Claude's accuracy when working with images by using the same kind of prompting techniques that we've already learned earlier on inside this course. So techniques like providing guidelines, providing analysis steps, or by using one shot or even multi-shot examples. So let me show you two ways in which we could very easily enhance this prompt and actually get back the correct result. And again, I actually tested this out and made sure that these examples, at least for me, worked as expected. So the first thing we might do is provide a series of steps for Claude to go through in analyzing the image. Now, of course, this is only really going to work if we kind of already understand the content of the image that we're feeding into Claude. So in this scenario, I might ask Claude to first take a look and try to identify each individual marble and just count each of them one by one. and then ask it to recount a second time to verify the initial count and provide it a different mechanism or different strategy for counting the number of marbles. And then finally at the bottom, I ask, okay, now let's kind of compare those two different counts and figure out what the correct answer is. So by providing a more sophisticated prompt, I was able to get results with a correct count of 12 marbles. Another technique we might use here is one shot or multi-shot prompting. So here's how that would work. Inside of my user message, I can alternate the presence of an image part and a text part. So in this scenario, I have an image part up here, a text part underneath it, and then another image, and then a text part. In the initial pair, I provide an image with 11 marbles, and then say very plainly, the image above has 11 marbles inside of it. Providing an example like this can easily improve Claude's accuracy when it goes to tackle your image later on. As usual, I would like to test out this feature in Claude inside of a Jupyter notebook. But this time around, we're going to have a little bit more complicated example. And I want you to understand the scenario that we're going to walk through here inside of our notebook ahead of time by showing you a quick diagram. All right, so here is a sample use case of how we might use Claude's image support capability. So in case you're not aware, in many parts of the United States, we have really bad wildfire problems, where wildfire will begin sweep through an area and burn down a ton of houses. And because this is a very common risk, a lot of people want fire insurance to ensure their home in case it gets burned down. But these insurers are very much aware that a house can absolutely be burned down tomorrow or next year or very shortly. So these insurers will very often require a homeowner who wants to ensure their home to trim trees or even cut trees down entirely around their house. Now the insurer needs to actually verify and make sure that the homeowner is taking care of the trees appropriately. But to verify that, they might have to send out a person to inspect each property and probably do that inspection maybe once every year or once every two years. That would become expensive really, really quickly. So one way that we can automate this process is by getting high resolution up to date satellite imagery and then feed it into Claude and ask Claude for a fire risk assessment. We might ask Claude in particular to try to detect the main residence on the property. So in other words, inside of a satellite image of a property, find the main home that is presumably insured. And then take a look for maybe tree branches that are overhanging the residence, which is a very common risk of fire. Maybe try to gauge how difficult it is for fire services to actually access the residence. So make sure in other words, there's kind of a clear path to get to the home and also take a look at the trees around the home and make sure that they are not too closely or tightly packed, which in its own right could be a fire risk as well. All right, so let's go over to notebook and see how we could implement this. I'm inside of a new notebook called 002 images. Inside of here, I have already put together a starter prompt for us. Now notice that this prompt is highly detailed and walks Claude through different points or different ideas that I want analyzed inside the image. I could have written out a very simple prompt of something like provide a fire score based upon the satellite image of this property and just left it there. I can almost guarantee you I would not get a good result. So instead, I applied some of the different prompt engineering techniques we've learned about previously, and I provided a series of different analysis steps for Claude to go through. Step 1. First, find the actual primary residence inside of the satellite photo. Step 2. Take a look at the tree density. Then take a look at the ability for fire services to actually access the property. Take a look at how many trees or specifically branches are overhanging the roof, which is a very common fire risk, and then finally assign a fire risk rating based upon all these different qualities. And I provide some criteria on helping it decide whether it should be a 1, 2, 3, or 4. And then finally at the very bottom, write a one-cent summary for each with a final score. So that's our prompt. I'm going to make sure I run that cell. And then let's go down here to the bottom. And we're going to write out some code to read in a sample image and feed it into Claude with that prompt and see what kind of result we get. One other quick item. Attach to this lecture, you will find a zip archive called images.zip. Make sure you extract that archive and place the images directory into the same folder as your notebook. This folder contains some different satellite imagery of different houses with some number of trees around it. So for example, Image 1 has a house with definitely a good amount of tree overhang. Image 2 has definitely a lot less trees, but there's still a little bit close tree right here to the property. And you can go through the rest and just verify that, yeah, we've definitely got some satellite imagery here. So our goal is going to be to send these different images into Claude and get a fire score rating for each. Back inside my notebook, I'm going to first begin by opening up an image file and converting its contents into base 64. So I'll do a width open. In the images directory, I'm going to look for image seven specifically. And I'm using that image in particular because it is absolutely surrounded by trees. So here's prop seven dot PNG. As you can see, definitely a lot of issues with fire here. I'm going to get the image files as base 64, standard underscore B64 and code. I'm going to pass an F dot read and I'll decode into utf-8. I'm then going to add in an empty list of messages. I'll add a user message into it. And this message that I am adding in is going to have two separate blocks. It is first going to have an image block, exactly with the structure that you see right here, and it will have a text block. And a text block is going to contain the actual directions that I want to feed into Claude. So I'll add in first a dictionary to represent the image block. So a type of image with a nested dictionary assigned to source that has a type of base 64, a media underscore type of image slash PNG. and data that's going to be the image bytes encoded as base 64. Then after that dictionary, I'll add in my actual prompt. So I'll give this a type of text. And then the prompt that I want to send in, I assign to the prompt variable right there. So I'll do a text of prompt. All right, finally, I'll call chat and pass in my list of messages. I'm going to run this and let's see what we get. Looking at the response, I'm going to scroll down to the very bottom and I should see a fire risk rating. In this case, I got a fire risk of high or a score in particular of three. So I think Claude did a pretty reasonable job of evaluating all the trees around the main property and deciding that, yeah, there's probably going to be an issue here. Before we move on, there is one last thing I want to remind you around images. Getting good results out of Claude when feeding images in all comes down to your prompting technique. Just as we examined a lot different ways of improving your prompt when using plain text, those same techniques apply to the world of images as well. So I would really encourage you to always make sure that you put together a very well-developed and well-evaluated prompt. Because if you rely upon simple prompts like what I'm putting in right here, it's probably not going to work quite as well as you might expect.

---

## 🎬 トランスクリプト（日本語）

次に、Claude の高度な機能で調査していくのは、Claude の画像認識機能です。 ユーザーメッセージを Claude に送信する際に、オプションで含めることができます。 メッセージ内に画像を。Claude に頼むことができます。 これらの画像で想像できることは何でも。 例えば、画像に何が含まれているか教えてほしいと頼むことができます。 異なる画像を比較するように頼むこともできます。Claude に頼むことができます。 異なるオブジェクトを数えるように。本当に多くの 可能性があります。まず理解してほしいのは 画像処理に関するさまざまな制限や要件です。 1回の送信で、最大 100 枚の画像を送信できます。 すべてのメッセージを通じて 単一のリクエスト。画像のサイズに関するいくつかの制限と 高さと幅にもあります。 そして 最後に、画像を送信すると常に トークン数としてカウントされることを理解する必要があります。 請求対象となります。数式があります。 ピクセル単位の画像の高​​さと幅に基づいて 請求されるトークン数を大まかに計算するために使用できます。 画像を Claude に送信するには、別の種類のブロックを含めます。 ユーザーメッセージ内に。これは画像ブロックです。 複数の異なる画像ブロックを1つの単一のユーザーメッセージに添付できます。 各画像ブロックは、単一の画像への参照を保持します。 この画像ブロック内で、生の画像データ、 または代わりに、オンラインでホストされている画像の URL を提供できます。 この技術的な制限と送信方法を理解したので 画像を送信する方法については、すぐにアドレス指定したい重要なことがあります。 エンジニアが Claude で画像の使用を開始すると、 非常に単純なプロンプトを使用し始めることに気づきます。 たとえこの例で提示したようなプロンプトであってもです。 画像を使用した Claude から良好な結果を得るための最も良い方法は、 プロンプト技術に重点を置くことです。 非常に単純なプロンプトと画像を入れるだけだと 多くの場合、良い結果は得られません。 例えば、右側の会話を見てみましょう。 12 個のビー玉が入った画像を入力しました。実際に テストして、非常に単純に尋ねました。 この画像には何個のビー玉がありますか？すると、予想通り 13 個という間違った数が返ってきました。 画像で作業する際の Claude の精度を劇的に向上させることができます。 以前にコースで学んだのと同じようなプロンプト技術を使用することで。 ガイドラインの提供、分析手順の提供、 または 1 ショットまたはマルチショットの例を使用するなどの技術です。 では、このプロンプトを非常に簡単に強化する方法を 2 つ示しましょう。 そして実際に正しい結果を得る方法。そして 再び、これらの例が少なくとも私にとっては期待通りに機能することを確認しました。 したがって、最初に行うことは、画像分析のために Claude が実行する一連の手順を提供することです。 もちろん、これは私たちが画像のコンテンツを 理解している場合にのみ機能します。 したがって、このシナリオでは、Claude にまず 調べて、それぞれのビー玉を個別に識別し、 1 つずつ数えるように依頼するかもしれません。そして、 もう一度数えて、最初のカウントを確認するように依頼し、 ビー玉の数を数えるための別のメカニズムまたは 戦略を提供します。そして最後に、 それらの 2 つの異なるカウントを比較して、正しい答えを見つけます。 したがって、より洗練されたプロンプトを提供することで、 12 個のビー玉という正しいカウントで結果を得ることができました。 もう 1 つの技術は、1 ショットまたはマルチショットのプロンプトを使用することです。 それがどのように機能するかを以下に示します。 ユーザーメッセージ内で、画像ブロックとテキストブロックを交互に配置できます。 したがって、このシナリオでは、上に画像ブロックがあり、 その下にテキストブロックがあり、次に別の画像と テキストブロックがあります。最初のペアでは、 11 個のビー玉が入った画像を提供し、それから 画像には 11 個のビー玉が含まれています。このように例を提供すると、 Claude の精度を簡単に向上させることができます。 画像で作業するとき。いつものように、ジュピターノートブック内で この機能をテストしたいと思います。しかし、今回は もう少し複雑な例になります。 そして、ノートブック内でこれから実行するシナリオを、 まず簡単な図を示して理解してほしいと思います。 さて、これは Claude の画像サポート機能の使用方法のサンプルユースケースです。 ご存じないかもしれませんが、アメリカの多くの地域では、 深刻な山火事の問題があり、山火事が 地域を焼き尽くし、多くの家を焼失させます。 これは一般的なリスクであるため、多くの人が火災保険を求めています。 万が一焼き失くされた場合に自宅を保険するために。しかし、 これらの保険会社は、家が明日、来年、 または非常に近いうちに焼き失くされる可能性があることを非常によく認識しています。 そのため、これらの保険会社は非常に頻繁に 家を保険したい家主に対して、木を刈り取るか、 または自宅の周りの木を完全に伐採するように要求します。 今や保険会社は、家主が適切に木の手入れをしていることを 確認する必要があります。しかし、それを検証するために、 検査のために人を派遣する必要があるかもしれません。 各物件を検査し、おそらく年に 1 回か 2 年に 1 回検査するでしょう。 それは非常に高価になるでしょう。 本当に早く。そのため、このプロセスを自動化する 1 つの方法は、高解像度の最新の衛星画像を取得し、 それを Claude に読み込ませて、火災リスク評価を依頼することです。 特に Claude には、物件の主要な住居を検出するように依頼するかもしれません。 つまり、物件の衛星画像内で、おそらく保険されている主要な家を見つけてください。 そして、住居にかかっている木の枝がないか見てみてください。 これは非常に一般的な火災リスクです。 火災サービスが実際に住居にアクセスするのを、 どの程度難しくするかを測定してみてください。 つまり、家にたどり着くための明確な道があることを確認してください。 そして、家の周りの木を見て、それらが近すぎたり 密集しすぎていないことを確認してください。 これはそれ自体が火災リスクとなる可能性があります。 では、ノートブックに移って実装方法を見てみましょう。 新しいノートブック 002 images にいます。 ここでは、スタータープロンプトをすでに用意しています。 このプロンプトは非常に詳細で、Claude に 画像内で分析してほしいさまざまなポイントやアイデアを伝えています。 単純なプロンプトで何かを書いて、 この物件の衛星画像に基づいて火災スコアを提供してください。 そしてそれをそのままにしておくこともできます。 ほぼ保証できますが、良い結果は得られなかったでしょう。 代わりに、以前に学んだプロンプトエンジニアリング技術のいくつかを適用し ました。そして、Claude が実行すべき一連の分析手順を提供しました。 ステップ 1。まず、衛星写真内の実際の主要な住居を見つけます。 ステップ 2。木の密度を見てください。次に、 火災サービスが物件にアクセスできるかどうかを見てください。 屋根にかかっている木の数、特に枝の数を見てください。 これは非常に一般的な火災リスクです。 そして最後に、これらのさまざまな特性すべてに基づいて 火災リスク評価を割り当てます。 そして、それが 1、2、3、または 4 のいずれであるかを判断するのに役立つ基準を提供します。 そして最後に一番下に、それぞれに 1 セントの要約と最終スコアを書いてください。 それが私たちのプロンプトです。セルを実行します。 そして、下にスクロールして、サンプル画像を読み込んで Claude にそのプロンプトと共にフィードして、どのような結果が得られるか見てみましょう。 もう 1 つのクイックアイテム。この講義には、images.zip という zip アーカイブが付いています。 そのアーカイブを解凍して、images ディレクトリを ノートブックと同じフォルダーに配置してください。このフォルダーには、 さまざまな家と周りの木の数が含まれる さまざまな衛星画像が含まれています。 たとえば、画像 1 は、間違いなくかなりの量の木のせり出しがある家です。 画像 2 は間違いなく木の量が少ないですが、 依然として物件のすぐ近くに木があります。 そして、残りの画像をすべて確認できます。 はい、衛星画像があります。 私たちの目標は、これらのさまざまな画像を Claude に送信し、 それぞれに火災スコアリングを行うことです。 ノートブックに戻り、まず画像ファイルを開いて そのコンテンツを base64 に変換することから始めます。 width open を実行します。 images ディレクトリの画像 7 を特に探します。 そして、特にその画像を使用しています。 なぜなら、それは間違いなく木に囲まれているからです。 ここに prop 7.png があります。ご覧のとおり、 間違いなく火災の問題があります。 画像ファイルを base64、standard_b64 として取得します。 そしてエンコードします。 f.read を使用し、utf-8 にデコードします。 次に、空のメッセージリストを追加します。 ユーザーメッセージを 1 つ追加します。 そして、このメッセージには 2 つのブロックが含まれます。 まず、画像ブロックが含まれます。 正確にこの構造で。そしてテキストブロックも含まれます。 テキストブロックには、Claude にフィードしたい実際の指示が含まれます。 そのため、まず画像ブロックを表す辞書を追加します。 画像のタイプ。 source にネストされた辞書が割り当てられ、 type は base64、media_type は image/png。 そして data は base64 でエンコードされた画像バイトです。 その後、その辞書の後に実際のプロンプトを追加します。 したがって、type は text にします。 そして、送信したいプロンプトは、その prompt 変数に割り当てます。 なので、text prompt とします。 よし、最後に chat を呼び出してメッセージリストを渡します。 これを実行して結果を見てみましょう。 応答を見て、一番下までスクロールすると、 火災リスク評価が表示されるはずです。 この場合、火災リスクは高またはスコア 3 でした。Claude は、主要な物件の周りのすべての木を評価し て、はい、ここに問題があるだろうと判断したのは、 かなり妥当だったと思います。 次に進む前に、画像に関してもう 1 つだけ思い出したいことがあります。 画像を Claude にフィードする際に良い結果を得ることはすべて、 プロンプト技術にかかっています。 プレーンテキストを使用するときにプロンプトを改善するさまざまな方法を たくさん調査したのと同様に、それらの同じ技術は 画像の世界にも適用されます。 だから私はあなたが常に非常に詳細で 評価されたプロンプトを作成するようにしてください。 なぜなら、もし私がここに入れているような単純なプロンプトに頼るなら、 それは期待しているほどうまく機能しないでしょう。
