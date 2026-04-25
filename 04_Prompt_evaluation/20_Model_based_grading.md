# 20. Model based grading

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287742
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Model based grading
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building prompt evaluation workflows, grading systems provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1 and 10, where 10 represents high quality and 1 represents poor quality.

Types of Graders

There are three main approaches to grading model outputs:

Code graders - Programmatically evaluate outputs using custom logic
Model graders - Use another AI model to assess the quality
Human graders - Have people manually review and score outputs

Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

Checking output length
Verifying output does/doesn't have certain words
Syntax validation for JSON, Python, or regex
Readability scores

The only requirement is that your code returns some usable signal - usually a number between 1 and 10.

Model Graders

Model graders feed your original output into another API call for evaluation. This approach offers tremendous flexibility for assessing:

Response quality
Quality of instruction following
Completeness
Helpfulness
Safety

Human Graders

Human graders provide the most flexibility but are time-consuming and tedious. They're useful for evaluating:

General response quality
Comprehensiveness
Depth
Conciseness
Relevance

Defining Evaluation Criteria

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

Format - Should return only Python, JSON, or Regex without explanation
Valid Syntax - Produced code should have valid syntax
Task Following - Response should directly address the user's task with accurate code

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

Implementing a Model Grader

Here's how to build a model grader function:

def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = """
    You are an expert code reviewer. Evaluate this AI-generated solution.
    
    Task: {task}
    Solution: {solution}
    
    Provide your evaluation as a structured JSON object with:
    - "strengths": An array of 1-3 key strengths
    - "weaknesses": An array of 1-3 key areas for improvement  
    - "reasoning": A concise explanation of your assessment
    - "score": A number between 1-10
    """
    
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)

The key insight is asking for strengths, weaknesses, and reasoning alongside the score. Without this context, models tend to default to middling scores around 6.

Integrating Grading into Your Workflow

Update your test case runner to call the grader:

def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Grade the output
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]
    
    return {
        "output": output, 
        "test_case": test_case, 
        "score": score,
        "reasoning": reasoning
    }

Finally, calculate an average score across all test cases:

from statistics import mean

def run_eval(dataset):
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")
    
    return results

This gives you an objective metric to track as you iterate on your prompt. While model graders can be somewhat capricious, they provide a consistent baseline for measuring improvements.
                        

---

## 🎬 Transcript (English)

The next thing we're going to implement inside of our prompt evaluation workflow is a grading system. As a reminder, a grader is going to take in some output coming from our model. And then our hope is that the grader is going to give us some kind of objective signal. It might be a number or a true or false value. It could be really anything, but very commonly, very frequently, you're going to see a number output between 1 and 10. where 10 means that we got a very high quality output, and one means we got a very low quality output. Again, that's not a requirement. We don't have to get numbers out of these graders, but it's a very common practice that you're going to see very often. There's three different kinds of graders that we're going to discuss in this video. Code, model, and human. Let's first figure out what code-based graders are all about. With a code-based grader, we're going to take the output from our model and feed it into a snippet of code that you and I author. Inside this code, we can do just about any kind of programmatic check you can imagine. So we might verify to make sure that the output from the model was not too long or too short. We might make sure that the output does have or doesn't have certain words. If we are returning JSON or code, we can do syntax validation programmatically, and we can even do more complex checks like implement a readability score, where we make sure that the generated text is at an appropriate reading level for our particular use case. The only requirement here is that when we run this code, we return some kind of actual signal we can use. And again, usually that's going to be a number between 1 and 10, but that is not a requirement. The next kind of grader that you're going to see very often is a model-based grader. This is where we take the output from our original model call, so the one that we already made, and we feed it into an additional model. So this is another API request. When we use a model grader, we get a tremendous amount of flexibility. We can ask a model to evaluate a response based upon its general quality, maybe how well it followed prompt instructions, maybe the completeness of the response, really just about anything you can imagine. Once again, the only real requirement here is that the model gives us back some kind of hard objective signal, usually as a number between one and 10. And then finally, human-based grading. With human-based grading, we're going to take all the outputs from our model and then put them in front of an actual person. This person is then going to be in charge of evaluating these responses in some particular way. As you can imagine, humans are very flexible, so we can ask them to evaluate responses in just about any fashion or for any metric you can possibly imagine. The one big downside to human-based grading is that it generally does take a lot of time, and it's certainly very tedious work. Now, no matter what style of grading you are using, you need to decide upfront what your evaluation criteria is going to be. So in other words, exactly what aspects of these responses are you going to be focusing on? For our particular use case, I've centered on three different evaluation criteria. I think first off, we should evaluate the responses to make sure that we're only getting back Python, JSON, or regular expression without any additional explanation being provided by Claude. Secondly, whenever we get that Python JSON or regex, we should make sure that it has some valid syntax so that there should be no typos in there or anything like that. And then finally, we should probably do some general task following and make sure that the model clearly addressed the user's task and answered it with some generally accurate code that doesn't contain any major errors or logic mistakes. So for these three different evaluation criteria, I think we can evaluate the first two with a code grader. So we can evaluate the format and make sure we got actual Python JSON or regex with code. And we can also validate the syntax of that code using well, additional code. And then finally, the general response and making sure that the user's question was clearly addressed, that would be more appropriate to address through a model grader given its flexibility. All right, let's start to implement first the model grader because that's believe it or not can be the easiest one to put together. I'm going to first begin by going back over to my notebook. I'm going to find that to do. We had put together right here inside of our run test case function. And then right above that cell, I'm going to add a new cell with a function that I'm going to call grade by model. And I'm going to assume that I'm going to pass in my test case dictionary. Remember, the test case dictionary is essentially these objects right here. Each of these data set values, these are our test cases. I'm also going to pass in the output from our original model call. And then inside of here, we're going to essentially make a call off to a model and ask it to grade the output. So for this, we usually end up writing a fairly long prompt. And again, just to save us a little bit of time, I'm going to copy paste a prompt in. So here we go. I'm going to paste this in. And yes, it is a little bit long, but this is kind of the bare minimum of what we want. So this prompt is going to set a role. It's then going to ask very clearly for the model to evaluate a AI generated solution. We're then going to print out the task. We're then going to list out the solution that was generated by the model. And then we're going to provide some directions on exactly how to respond. In this particular case, I'm asking the model to give me a list of strengths and weaknesses of the AI generated solution, along with some reasoning behind that and an actual score. Now we could just ask for a score by itself, but if you do so, you're gonna see very often you tend to get scores of just six. So if you don't ask for any additional strengths or weaknesses or reasoning, you're gonna very often just get very middling scores because the model kind of assumes, well, could be better, could be worse, we'll give it a six. By asking the model to provide some reasoning, strengths and weaknesses, you really make it hone in and decide upon a more concrete score. So now that we have that prompt in here, I'm going to call our additional grading model. So right underneath it, I'll again make a messages list. I'll add in a user message. And then because we are getting back some JSON here, we need to once again, make sure we extract that cleanly by using a pre-filled assistant message and a stop sequence. So we'll add a assistant message. with `json` JSON, and then I'll get back some eval text, and we'll call chat with messages and a stop sequence or stop sequences of, once again, closing `json`. Now this eval text should be a JSON object with this kind of structure right here. So I'm going to parse that and just return it. So return a JSON dot loads with eval text. Okay, so that is our model grader. That's really all it takes to at least get started. So now we need to make sure we actually call this grader to call the grader. I'll go down to our to do right here. I'm going to replace score with model grade. And that's going to be coming from our grade by model function. And remember, we have to pass in the test case, along with the output from actually running the prompt. And then from this, we're going to get a score from model grade. And I'm also going to extract from that dictionary that gets returned the reasoning behind the score. Inside of this model grade dictionary that we are returning, there is also going to be the strengths and weaknesses list. You could definitely extract those as well as you want, but I'm just going to keep our example a little bit more concise. I'm going to take the score and reasoning and put them into this final output dictionary. So I will add in some additional keys here of score. Oh, I already have score right there. My mistake. I don't need that, but I do need reasoning. And that will be reasoning. Okay, so that looks good. I'm not going to make sure I run these cells. I'm going to run that one, update run test case. And then I'm going to rerun my actual evaluation. That is going to take a while to complete. For me, it takes about 22 seconds this time around. And now if I print out those results, let's see what we get. So I've now got the generated output here. And if I scroll down a little bit, I can take a look at the score that was generated by the model and some reasoning behind that score. So in this case, I got an eight. That's not bad. And that's why I got the eight. And if I keep going down, the next one got a seven. And then finally, I got a six. So the last thing we would probably want to do here is take all these scores, add them together, get an average, and print that out. So we get a final, very objective score to tell us how well our prompt is currently functioning. So to average all these scores out and print the results, I'm going to find the run eval function right here. And I will calculate the average score with a comprehension of result score for result in results. And I'm going to wrap that with a mean function call. And then I will import the mean function from the statistics package. One last step. Let's make sure we actually print out that average score. We'll do a print. average score like so. All right, now I'm going to run this code just one more time to make sure everything is working as expected. And after it runs, I see that I do get, in fact, an average score of 7.33. And once again, this gives us finally an actual objective metric. Yeah, it's being graded by a model that might be a little bit capricious sometimes. And maybe we could give better guidance on how to grade things, but at least we have a score that we can start to focus on and try to increase.

---

## 🎬 トランスクリプト（日本語）

次にプロンプト評価内で実装するのは、採点システムです。 リマインダーとして、グレーダーはモデルからの何らかの出力を受け取ります。 そして、グレーダーが何らかの客観的なシグナルを 私たちに提供してくれることを期待しています。数値や真偽値になる かもしれません。何でも構いませんが、非常に一般的で、頻繁に 見られるのは、1から10の間の数値出力です。 10は非常に高品質な出力を得られたことを意味し、1は非常に低品質な出力を得られたことを意味します。 繰り返しますが、それは要件ではありません。数値を得る必要はありません。 グレーダーから、しかし、それは非常に一般的な慣行です。 それは非常に頻繁に見られるでしょう。このビデオでは3種類のグレーダーについて説明します。 コード、モデル、そして人間です。まず コードベースのグレーダーがどのようなものかを理解しましょう。 コードベースのグレーダーでは、モデルからの出力を 受け取り、それをあなたと私自身が作成したコードのスニペットに 入力します。このコード内で、プログラム的な チェックはほとんど何でもできます。例えば、モデルからの出力が 長すぎないか、短すぎないかを確認することもできます。 また、特定の単語が含まれているか、含まれていないかを確認することもできます。 JSONやコードを返す場合は、構文検証をプログラム的に行うこともできますし、 読みやすさスコアの実装のような、より複雑なチェックも可能です。 生成されたテキストが、特定のユースケースに対して 適切な読みやすさレベルであることを確認するものです。 ここでの唯一の要件は、このコードを実行したときに 何らかの実際の使用可能なシグナルを返すことです。 そして通常それは1から10の間の数値ですが、それは要件ではありません。 次によく見られるグレーダーは モデルベースのグレーダーです。これは、 元のモデル呼び出しからの出力を受け取り、 それを追加のモデルに入力するということです。 これは別のAPIリクエストです。モデルグレーダーを使用すると、 計り知れない柔軟性が得られます。モデルに、 その一般的な品質、おそらくプロンプトの指示にどれだけ従ったか、 または応答の完全性に基づいて応答を評価するように依頼できます。 想像できるほぼすべてのことです。 ここでの唯一の本当の要件は、モデルが何らかの 客観的なシグナルを返してくれること、通常は 1から10の間の数値です。そして最後に、 人間ベースの採点です。人間ベースの採点では、 モデルからのすべての出力を受け取り、それを 実際の人の前に置きます。その人はこれらの応答を 特定の方法で評価する責任を負います。 想像できるように、人間は非常に柔軟なので、応答を あらゆる方法やあらゆるメトリックで評価するように依頼できます。 人間ベースの採点の1つの大きな欠点は、一般的に 時間がかかり、間違いなく非常に手間のかかる作業であることです。 さて、どの採点スタイルを使用する場合でも、 評価基準が何になるかを事前に決定する必要があります。 つまり、具体的にこれらの応答の どの側面に着目するのでしょうか？ 今回のユースケースでは、私は3つの異なる評価基準に焦点を当てました。 まず、応答を評価して、Python、JSON、 または正規表現のみを、追加の説明なしに Claudeから受け取っていることを確認すべきです。 次に、そのPython、JSON、または正規表現を受け取った場合は、 それらが有効な構文を持っていることを確認する必要があります。 そのため、タイプミスなどがないはずです。 そして最後に、一般的なタスク実行を行い、 モデルがユーザーのタスクを明確に実行し、 一般的に正確で、主要なエラーや論理的な間違いを含まないコードで 回答したことを確認すべきです。 これらの3つの異なる評価基準について、 最初の2つはコードグレーダーで評価できると思います。 つまり、形式を評価し、実際のPython、JSON、 または正規表現を取得したことを確認できます。 そして、コードの構文も、まあ、追加のコードを使用して 検証できます。 そして最後に、一般的な応答と、ユーザーの質問が 明確に実行されたことを確認することは、 その柔軟性を考慮すると、モデルグレーダーを通じて対処する方が適切でしょう。 よろしい、まずモデルグレーダーを実装しましょう。 なぜなら、信じられないかもしれませんが、それは最も簡単なものになるからです。 まずノートブックに戻ります。 テストケースを実行する関数の中に 入れた、あの「やること」を見つけます。 そして、そのセルのすぐ上に、 `grade_by_model`と呼ぶ関数を持つ新しいセルを追加します。 そして、テストケースの辞書を渡すと仮定します。 テストケースの辞書は、基本的にこれらの オブジェクトです。データセットの各値、 これらが私たちのテストケースです。また、 最初のモデル呼び出しからの出力を渡します。 そしてここでは、基本的にモデルに電話して 評価するように依頼します。そのためには、 かなり長いプロンプトを書きます。 そしてまた、時間を節約するために、コピー＆ペーストします。 プロンプトを貼り付けます。ここです。 これを貼り付けます。はい、少し長いですが、 これは私たちの欲しいものの最低限のものです。 このプロンプトはロールを設定し、次にモデルに AI生成のソリューションを評価するように明確に依頼します。 次にタスクを出力し、次にモデルが生成した ソリューションを一覧表示します。 そして、応答する方法について指示を提供します。この 特定のケースでは、モデルにAI生成ソリューションの 長所と短所のリストと、その理由、 そして実際のスコアを提供するように求めています。 スコアだけを求めることもできますが、そうすると 多くの場合6というスコアしか得られないでしょう。 追加の長所や短所、または理由を求めない場合、 モデルは、まあ、もっと良くなるかもしれない、悪くなるかもしれないと 仮定するので、しばしば中間的なスコアしか得られません。 6を与えましょう。モデルに理由、長所、短所を 提供するように依頼することで、 より具体的なスコアを決定するように促すことができます。 これでプロンプトができたので、追加の採点モデルを呼び出します。 その下に、メッセージのリストを作成します。 ユーザーメッセージを追加し、 そして、ここでJSONを受け取るので、 事前に用意されたアシスタントメッセージと 停止シーケンスを使用して、それをきれいに抽出するように 再度確認する必要があります。 アシスタントメッセージを追加します。`json`で JSON、 そして評価テキストを受け取り、 メッセージと停止シーケンスでチャットを呼び出します。 停止シーケンスは、再度、`json`の閉じ括弧です。 この評価テキストは、 この構造のJSONオブジェクトであるべきです。 それを解析して返すだけです。 JSON.loadsで評価テキストを返すだけです。 はい、これでモデルグレーダーは完了です。 少なくとも始めるにはそれだけで十分です。 これで、このグレーダーを実際に呼び出すことを確認する必要があります。 グレーダーを呼び出すために、あの「やること」までスクロールします。 スコアをモデルグレーダーに置き換えます。 そしてそれは`grade_by_model`関数から来ています。 そして、テストケースと、 プロンプトを実行した結果の出力を渡す必要があることを覚えています。 そして、これからモデルグレーダーからスコアを得ます。 そして、返されるその辞書から、 スコアの理由を抽出します。 返すモデルグレーダーの辞書の中には、 長所と短所のリストも含まれています。 もちろん、それらも必要に応じて抽出できますが、 例をもう少し簡潔にするために、 スコアと理由を取得して、これらの最終的な 出力辞書に入れます。 追加のキーをここにいくつか追加します。 スコア。ああ、スコアはもうありますね。私の間違いです。 それは必要ありませんが、理由は必要です。 それは理由になります。 よし、これで良さそうです。これらのセルを実行することを確認します。 それを実行して、テストケースの実行を更新します。 そして、実際の評価を再度実行します。 それは完了にしばらく時間がかかります。 私の場合、今回は約22秒かかります。 そして今、結果を出力すると、 何が得られるか見てみましょう。 生成された出力がここにあります。 そして少しスクロールすると、モデルによって生成された スコアと、そのスコアの理由を見ることができます。 この場合、8を得ました。それは悪くないです。 そして、それが私が8を得た理由です。 そして、下に続けていくと、次のものは7を得ました。 そして最後に、6を得ました。 ですから、私たちがここで行うべき最後のことは、これらのスコアすべてを 合計し、平均を求めて、それを表示することです。 そのため、プロンプトが現在どの程度機能しているかを 示すための最終的な客観的な指標が得られます。 これらのスコアすべてを平均して表示するために、 実行評価関数を見つけます。 そして、結果のスコアの包括的な方法で平均スコアを計算します。 結果の`mean`関数呼び出しでラップします。 そして、`mean`関数を統計パッケージからインポートします。 最後のステップです。平均スコアを実際に表示するようにしましょう。 次のように、print average scoreを行います。 よし、 これで、すべてが期待どおりに動作することを確認するために もう一度コードを実行します。 実行後、平均スコアが7.33であることを確認できます。 そしてまた、これにより最終的に 客観的な指標が得られます。 はい、それはモデルによって採点されています。 それは時々少し気まぐれかもしれません。 そして、採点方法を改善できるかもしれませんが、 少なくとも、私たちが焦点を当てて増やそうとできる スコアがあります。
