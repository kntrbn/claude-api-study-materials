# 17. A typical eval workflow

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287736
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    A typical eval workflow
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

prompt = f"""
Please answer the user's question:

{question}
"""

This basic prompt will serve as our baseline for testing and improvement.

Step 2: Create an Eval Dataset

Your evaluation dataset contains sample inputs that represent the types of questions or requests your prompt will handle in production. The dataset should include questions that will be interpolated into your prompt template.

For this example, our dataset includes three questions:

"What's 2+2?"
"How do I make oatmeal?"
"How far away is the Moon?"

In real-world evaluations, you might have tens, hundreds, or even thousands of records. You can assemble these datasets by hand or use Claude to generate them for you.

Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude to get responses.

For example, the first question becomes:

Please answer the user's question:
What's 2+2?

Claude might respond with "2 + 2 = 4" for the math question, provide oatmeal cooking instructions for the second question, and give the distance to the Moon for the third.

Step 4: Feed Through a Grader

The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.

In our example, the grader might assign:

Math question: 10 (perfect answer)
Oatmeal question: 4 (needs improvement)
Moon question: 9 (very good answer)

The average score across all questions gives you an objective measurement: (10 + 4 + 9) ÷ 3 = 7.66

Step 5: Change Prompt and Repeat

Now that you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.

For example, you might add more guidance to your prompt:

prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""

After running this improved prompt through the same evaluation process, you might get a higher average score of 8.7, indicating that the additional instruction helped Claude provide better responses.

Prompt Scoring

The key benefit of this workflow is getting objective measurements of prompt performance. You can:

Compare different prompt versions numerically
Use the version with the best score
Continue iterating to find even better approaches

This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.

---

## 🎬 Transcript (English)

In this video, we're going to walk through all these steps implemented by a typical prompt evaluation workflow. Before we go through any of these steps, however, I just want you to understand two important things. First is, there are many different ways you can assemble a workflow. There's no one set methodology set in stone that is standard across the industry. The second thing to understand is that there are many different open source packages and even paid options online that will help you implement your own workflows. Now, in this video and this module, we're going to start to implement our own custom workflow from scratch inside of a Jupyter notebook. The reason we're doing this is to, of course, just help you understand how these workflows behave, but also to help you understand that you don't have to get a really heavy weight solution to do prompt evals. You can start small just to get started and get a sense of how everything works and then scale up from there. All right, so let's get to it. Step one of a typical prompt eVal. Step one, we're going to write out an initial prompt draft. So you and I will sit down and just write out some kind of prompt that we want to improve in some way. For this example, we're going to have a very simple prompt that just says, please answer the user's question. And then we're going to interpolate in some user input. So some question provided by a user. In step two, we're going to create an evaluation data set. This data set is going to contain some number of possible inputs that we might want to put into our prompt. So for us, our prompt only has one input, a question provided by user. So for our Eval data set, we'll have a list of different possible questions that we might want to put into our prompt. My data set is only going to have three different questions inside of it. But in real-world Evals, you might have tens, hundreds, even thousands of different records in your data set. Now you can assemble these data sets by hand, or you can of course also use Claude to generate them for you. Once we have our eval dataset, we're then going to feed each of these different questions into our prompt. So we get a fully fleshed out prompt that we can then feed into Claude. So we might have prompt one right here, where we have, please answer the user's question, and then a sample question out of our dataset, like what's two plus two? And then we will repeat for all the other records inside of our dataset. So yours two and three. We'll then feed each of these into Claude and get an actual response out of Claude. So for the first one, we might get back a response of something like 2 plus 2 is 4, and then something about how to make oatmeal, and then something about the distance to the moon. Once we have these actual answers coming out of Claude, we're then going to grade them in some way. During this grading step, we're going to take each of the questions out of our data set, and the answers we got out of Claude. We'll pair them all off together, and we'll feed them into a grader one by one. There are many different ways we can implement this grader. We'll take a look at some of the different methodologies a little bit later. The grader will then give us a score, maybe from 1 up to 10, based upon the quality of the answer that was produced by Claude. So a 10 would mean we got a perfect answer and there's really no possible way we could improve it. And maybe something like a 4 indicates that there's definitely room for improvement there. Now, as you can guess, there's kind of a lot of hidden complexity here with a grader, because you're probably curious or wondering, well, how do we actually get these scores at all? And again, don't worry. We're going to cover these grader things in much greater detail in a little bit. After we get these scores, we're then going to average them all together. So in this case, I would add the scores together, divide by three, and get an average score of 7.66. So I now have some kind of objective way of describing how well our original prompt performed. Now that we have this score, we can then change our prompt in some way and iterate or repeat this entire process. So if I want to improve my score, I might try adding in a little bit more detail to the prompt to hopefully guide Claude a little bit more and help to understand what kind of output we want. So maybe I would add on to the end of the prompt, something like answer the question with ample detail. Once I have the second version of my prompt, I would then run it through this entire pipeline again. I would then have a score for prompt version one and prompt version two. I could then compare these two scores and whichever score is greater or higher. It's kind of an objective sign, better than nothing that tells me that prompt V2 in this case is perhaps the better version of our prompt. So now that we have a high level overview of this entire process, as I mentioned, we're gonna start to implement our own custom eval framework inside of a Jupyter notebook. So let's get started on an implementation in the next video.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、これらすべてのステップを実装する手順を説明します。 典型的なプロンプト評価ワークフローで実行します。 これらのステップのいずれかを実行する前に、理解しておきたいことが2つあります。 まず、ワークフローを組み立てる方法はたくさんあります。 業界全体で標準化された方法論はありません。 確立された方法論はありません。 業界全体で標準化された方法論はありません。 理解すべき第二の点は、多くの異なるオープンソースパッケージや 有料のオンラインオプションがあり、これらが独自のワークフローの実装に役立つことです。 さて、このビデオとこのモジュールでは、 ジュピターノートブック内で独自のカスタムワークフローをゼロから実装し始めます。 ジュピターノートブックでゼロから独自のカスタムワークフローを実装し始めます。 これを行う理由は、もちろん、これらのワークフローがどのように動作するかを理解するのに役立つだけでなく、 プロンプト評価を行うために、本当に重いソリューションを取得する必要はないことを理解するのに役立つためです。 始めるために小さく始めて、すべてがどのように機能するかを把握することができます。 そして、そこからスケールアップできます。さあ、始めましょう。 典型的なプロンプトEvalのステップ1。 ステップ1では、初期のプロンプトドラフトを書き出します。 あなたと私は座って、改善したい何らかのプロンプトを書き出します。 この例では、ユーザーの質問に答えてくださいという非常にシンプルなプロンプトを使用します。 そして、ユーザーの入力、つまりユーザーが提供した質問を補間します。 ステップ2では、評価データセットを作成します。 このデータセットには、プロンプトに入れる可能性のあるいくつかの入力が含まれます。 したがって、私たちのプロンプトにはユーザーから提供された1つの質問しかありません。 したがって、私たちのEvalデータセットには、プロンプトに入れる可能性のあるさまざまな質問のリストがあります。 私のデータセットには3つの異なる質問しか含まれていません。 しかし、実際のEvalでは、データセットに数十、数百、あるいは数千のレコードがあるかもしれません。 これらのデータセットを手動で作成することもできますし、 Claudeを使用してそれらを生成することもできます。 Evalデータセットが作成されたら、 これらの異なる質問をそれぞれプロンプトにフィードします。 したがって、Claudeにフィードできる完全に詳細なプロンプトが得られます。 ここではプロンプト1があり、ユーザーの質問に答えてください。 そして、データセットからのサンプルの質問は何ですか？ たとえば、2プラス2は何ですか？ そして、私たちは残りのレコードすべてに対してこれを繰り返します。 したがって、2番目と3番目のレコードも同様です。 これらをそれぞれClaudeにフィードして、実際の応答を取得します。 したがって、最初の応答として、2プラス2は4です。 そして、オートミールの作り方について。 そして、月までの距離について。 Claudeからこれらの実際の回答が得られたら、 それらを何らかの形で採点します。 この採点ステップ中に、データセットから質問をそれぞれ取り出し、 Claudeから取得した回答を取り出します。 それらをすべてペアにし、採点者に一つずつフィードします。 この採点者を実装する方法はたくさんあります。 少し後でさまざまな方法を見ていきましょう。 採点者は、Claudeによって生成された回答の質に基づいて、1から10までのスコアを付けます。 したがって、10は完璧な回答であり、改善の余地がないことを意味します。 そして、おそらく4のような値は、改善の余地があることを示しています。 さて、ご想像の通り、採点者には多くの隠れた複雑さがあります。 これらのスコアをどのように取得するのか疑問に思っているかもしれません。 そして、心配しないでください。採点者については後で詳しく説明します。 これらのスコアを取得したら、それらをすべて平均します。 この場合、スコアを合計して3で割ると、平均スコアは7.66になります。 したがって、元のプロンプトがどれだけうまく機能したかを記述するための客観的な方法が得られました。 このスコアが得られたので、プロンプトを変更して このプロセス全体を反復または繰り返すことができます。 したがって、スコアを改善したい場合は、プロンプトに少し詳細を追加して、Claudeをもう少しガイドし、 どのような出力が必要か理解するのを助けることができます。 したがって、たとえば、プロンプトの最後に、「十分な詳細で質問に答えてください」と追加します。 プロンプトの2番目のバージョンを入手したら、 このパイプライン全体を再度実行します。 プロンプトバージョン1とプロンプトバージョン2のスコアが得られます。 次に、これらの2つのスコアを比較できます。 どちらのスコアが高いか、あるいはより高いか。 これは、プロンプトV2がこのケースではプロンプトのより良いバージョンである可能性が高いことを示す客観的なサインです。 何もよりも。 したがって、このプロセスの全体像の概要を把握しました。 すでに述べたように、独自のカスタムEVALフレームワークを実装し始めます。 ジュピターノートブック内で。 次のビデオで実装を開始しましょう。
