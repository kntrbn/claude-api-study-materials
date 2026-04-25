# 28. Providing examples

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287746
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Providing examples
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

The challenge here is sarcasm. A tweet like "Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'" appears positive on the surface, but it's actually sarcastic and negative (Plan 9 is famously one of the worst movies ever made).

Adding Examples to Handle Corner Cases

To solve this, you can add examples that show Claude how to handle tricky cases:

The improved prompt includes:

A clear positive example: "Great game tonight!" → "Positive"
A sarcastic example: "Oh yeah, I really needed a flight delay tonight! Excellent!" → "Negative"
Context explaining why sarcasm should be treated carefully

Notice how the examples are wrapped in XML tags like <sample_input> and <ideal_output>. This structure makes it crystal clear to Claude what each part represents.

When to Use Examples

Examples are particularly useful for:

Capturing corner cases or edge scenarios
Defining complex output formats (like specific JSON structures)
Showing the exact style or tone you want
Demonstrating how to handle ambiguous inputs

One-Shot vs Multi-Shot

One-Shot: Provide a single example to establish the pattern
Multi-Shot: Provide multiple examples to cover different scenarios

Use multi-shot when you need to handle various edge cases or want to show different types of valid responses.

Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs to use as examples:

Find responses that scored 10 (or your highest available score) and use those input/output pairs as examples in your prompt. This helps Claude understand what "perfect" output looks like for your specific use case.

Adding Context to Examples

Don't just provide the input/output pair - explain why the output is good:

<ideal_output>
[Your example output here]
</ideal_output>

This example is well-structured, provides detailed information 
on food choices and quantities, and aligns with the athlete's 
goals and restrictions.

This additional context helps Claude understand the reasoning behind good responses, not just the format.

Best Practices

Always use XML tags to structure your examples clearly
Be explicit about what you're showing: "Here is an example input with an ideal response"
Include examples that address your most common failure cases
Explain why your example outputs are considered ideal
Keep examples relevant to your specific task

Examples are especially powerful because they show rather than tell. Instead of trying to describe exactly what you want in words, you demonstrate it directly. This makes your prompts much more reliable and helps Claude understand subtle requirements that might be hard to express in instructions alone.

---

## 🎬 Transcript (English)

I'm really excited about this next prompt engineering technique we're going to discuss because it is probably one of the most effective that you're going to find. It's the idea of providing examples inside of your prompt. This is often referred to as one-shot or multi-shot prompting, depending upon whether or not you are providing just one example or multiple examples. Understanding this concept is definitely easiest if you take a look and example, so let's do that right away. Consider the prompt on the right-hand side. I'm asking Claude to categorize the sentiment of a tweet. Just be clear, when we say sentiment, we mean kind of, does this seem kind of happy or positive in nature or unhappy or negative? In this particular instance, I provided an input tweet of, yeah, sure, that was the best movie I've ever seen since Plan 9 from Outer Space. Now if you're not aware, Plan 9 from Outer Space is a famously bad movie. So if someone were to tweet something like this, they're actually probably being sarcastic and they probably did not like the movie they just watched at all. So we would probably want to classify the tweet as being negative. But Claude could potentially have some issue categorizing this. One way to solve the problem would be by using multi-shot prompting. So here's how we would fix this. We would take our starting prompt we have on the left-hand side and add in some examples, which I've added in on the bottom half of the prompt right here. To add in an example, we will very directly tell Claude that we are about to give it some example input and an ideal, perfect world kind of response. We'll almost always wrap these inputs and outputs inside of some XML tags, just to better structure our prompt and make it super clear to Claude with the purpose of the input and output pair. So in this particular example, I have given a sample input of great game tonight, which I would say is definitely positive in nature. So right after that, I would then put in an ideal output of simply positive. This gives Claude a concrete objective example of how to deal with some kind of input. So now Claude knows that if it ever sees some kind of input like this again in the future, well, it should probably label it as positive because that's how it was done in the past. We can make use of multi-shot prompting, that's where we provide multiple different examples whenever we want to handle corner cases. And dealing with sarcastic tweets like this is definitely a corner case that we kind of want to highlight to Claude. When adding examples that highlight corner cases, add in some context to Claude, and tell it should be especially aware of certain scenarios. So for example, we might say, be especially careful with tweets that contain some sarcasm, and then provide an immediate example of that. So now, in this case, I've got an example tweet or a sample input of, oh yeah, I really need a flight delayed tonight, excellent. If you didn't understand the concept of sarcasm, this would seem like a positive sentiment tweet. But of course, we can probably understand that this is sarcasm and so it probably is actually negative. Once again, Claude can take a look at this example when grading our provided input up here, the original input, and Claude will have a better chance of recognizing that, oh yeah, this looks like it's sarcasm too, this is also probably negative in nature. Now, multi-shot prompting like this can be used not only for capturing corner cases or giving a little bit more clarity to Claude, but also helping Claude understand more complex output formats. So if you ever need to generate a JSON object that is rather complex in nature, you might provide a sample input and an example output and show that kind of complex JSON structure to Claude. And now it will have a better idea of the exact structure of output that it is going for. Providing examples is especially effective whenever you are doing prompt evals as we currently are. Remember whenever you run a prompt eval using our little framework inside the notebook, it creates an HTML file inside the same directory. So we can hunt through this file until we find a perfect 10, or hopefully just a test case with a rather high score. If I scroll through, I will find a 10 right here. Now, you might not have any tens inside of your output. If you don't, that's totally fine. Just try to find the record with the highest score. So this is an example of where we had some input and output that was gauged to be pretty much as good as we're going to get by our model grader. So we might decide to provide this as an example inside of our prompt. And hopefully, that will guide Claude to producing output that looks like this a little bit more often. Let's try this out. I'm going to copy this input right here. Go back over to my prompt. I'm going to scroll underneath the guideline section. And I'm going to explicitly tell Claude that I'm about to provide it an example that's going to contain a sample input and an ideal output. So I'll say here is a an example with a sample input and an ideal output. I'll then put in my sample input inside of XML tags. and an ideal output. And inside those tags, I'm going to go back over and copy paste the output from right here. I'll then paste it in like so and fix some indentation. Before we rerun our eval, there's one last thing I want to show you. This last step is completely optional, but I personally have had great success with it. It's often very beneficial to help Claude understand exactly why this is ideal output. If we go back over to our report, remember we have this last column over here that explains exactly why the grader thought that this was some ideal output. So we can copy just the kind of first half of some message over here where it says or lists out why this is a good response. Take that back over, and then underneath the closing ideal output tag, we could paste in that reasoning. And then maybe update the grammar just a little bit to say, this example meal plan is well structured, etc. So now Claude has a better idea of exactly why this is considered to be ideal output. And it's going to better reinforce the idea that Claude needs to return a well structured output that contains some detailed information on the food choices and quantities, and most importantly, matches the athlete's goals and restrictions. Okay, so let's now run that cell and then rerun our eval and see how we are doing. So I'm going to rerun this and are we going to go up or down. We end up going up just a little bit to 7.96. Well, let's wrap things up. As a reminder, this technique is often referred to as one shot or multi-shot prompting. One shot is where you provide a single example, multi-shot is where you provide multiple examples. And this is a technique you're going to very often use anytime you want to make sure Claude handles corner cases, or especially when you want Claude to make sure it matches some kind of complex output format.

---

## 🎬 トランスクリプト（日本語）

この次のプロンプトエンジニアリング手法についてお話しするのがとても楽しみです。 なぜなら、これはおそらく最も効果的な手法の一つだからです。 プロンプト内に例を提供することです。これはよく ワンショットまたはマルチショットプロンプティングと呼ばれます。 提供する例が1つか複数かによります。 この概念を理解するには、例を見るのが最も簡単です。 なので、すぐにそうしましょう。 右側のプロンプトをご覧ください。Claudeに ツイートの感情を分類するように求めています。 感情とは、どのようなものかと言うと、 幸せまたはポジティブな性質のものか、 それとも不幸せまたはネガティブなものか、 ということです。 この特定のインスタンスでは、入力ツイートとして 「ああ、 sure、それは今までで最高の映画だったよ、 『プラン9・フロム・アウタースペース』以来ね。」 を提供しました。 もしご存知ないなら、『プラン9・フロム・アウタースペース』は 悪名高い駄作映画です。もし誰かが このようなツイートをした場合、実際には皮肉を言っている可能性が高く、 見た映画は全く気に入らなかったのでしょう。 ですから、そのツイートはネガティブと分類したいでしょう。 しかし、Claudeはこれを分類するのに問題を抱える可能性があります。 その問題を解決する一つの方法は、マルチショットプロンプティングを使用することです。 なので、こうやって修正します。左側の 開始プロンプトに例を追加します。 このプロンプトの下半分に追加しました。 例を追加するには、 Claudeに、これから例の入力と 理想的な、完璧な世界の応答を 与えることを非常に直接的に伝えます。 これらの入出力は、プロンプトをより構造化し、 Claudeに目的を明確にするために、 XMLタグで囲むことがほとんどです。 この特定の例では、 サンプル入力として「素晴らしいゲームだったね、 今夜は。」を提供しました。これは明らかにポジティブです。 その直後に、理想的な出力として 単に「ポジティブ」と入力します。 これはClaudeに、 入力を処理する方法の具体的な例を与えます。 これでClaudeは、 もし将来このような入力を再び見た場合、 過去のやり方と同じように、ポジティブとラベル付けすべきだと知っています。 マルチショットプロンプティングを活用できます。 これは、複数の異なる例を提供することで、 コーナーケースを処理したい場合に使用します。 このような皮肉なツイートに対処するのは、 確かに強調したいコーナーケースです。 コーナーケースを強調する例を追加する際は、 Claudeにコンテキストを提供し、 特定のシナリオに特に注意するよう伝えます。 例えば、 皮肉を含むツイートには特に注意してください、 と言い、すぐに例を示します。 なので、ここでは、サンプルツイート、つまり入力は、 「ああ、ほんと、フライトが遅れてくれないかな、最高。」です。 もし皮肉の概念を理解していなければ、 これはポジティブな感情のツイートに見えるでしょう。 しかし、もちろん、 これは皮肉であり、実際にはネガティブである可能性が高いと 理解できるでしょう。再び、Claudeは ここにある入力と、 提供された入力を見て、この例を取ることができます。 そしてClaudeは、 「ああ、これは皮肉のようだな、これもネガティブだろう」と認識する可能性が高まります。 このようなマルチショットプロンプティングは、 コーナーケースを捉えるためや、 Claudeに少し明確さをもたらすために使用できるだけでなく、 Claudeがより複雑な出力形式を 理解するのを助けるためにも使用できます。 もし、かなり複雑なJSONオブジェクトを生成する必要がある場合、 サンプル入力と例の出力を提供し、 その種の複雑なJSON構造をClaudeに示すと良いでしょう。 これにより、Claudeは正確な構造を より良く理解できるようになります。例を提供することは、 特に現在行っているようなプロンプト評価では効果的です。 覚えておいてください、ノートブック内の 私たちの小さなフレームワークを使ってプロンプト評価を実行すると、 同じディレクトリにHTMLファイルが作成されます。 したがって、私たちはこのファイルを探して、 完璧な10、またはうまくいけば、 非常に高いスコアのテストケースを見つけます。 スクロールすると、ここに10を見つけます。 出力内に10がない場合でも問題ありません。 最も高いスコアのレコードを見つけてください。 これは、入力と 出力があった例です。 モデルグレーダーによって非常に良いと評価されました。 ですから、これを例として プロンプトに提供するかもしれません。 そして、Claudeがこのような出力を より頻繁に生成するように導くことを願っています。 試してみましょう。この入力をコピーします。 プロンプトに戻ります。 ガイドラインセクションの下にスクロールして、 Claudeに、これからサンプル入力と 理想的な出力を含む例を提供することを 明示的に伝えます。 「サンプル入力と理想的な出力の例」と言います。 次に、XMLタグの中にサンプル入力と 理想的な出力を入れます。 そしてタグの中に、ここから出力を コピー＆ペーストします。 このように貼り付けて、 インデントを調整します。 評価を再度実行する前に、もう一つお伝えしたいことがあります。 この最後のステップは完全に任意ですが、個人的には 大きな成功を収めています。 Claudeにこれがなぜ理想的な出力なのかを正確に理解させるのに、 非常に役立つことが多いです。 レポートに戻ると、ここにある最後の列を 思い出してください。グレーダーがなぜ これが理想的な出力だと考えたのかを正確に説明しています。 ですから、メッセージの最初の部分を コピーして、なぜこれが良い応答なのかを リストアップした部分を ここに戻って、閉じられた理想的な出力タグの下に、 その理由を貼り付けることができます。 そして、文法を少し修正して、 「この例のミールプランは よく構成されています、など」とします。 これでClaudeは、 これがなぜ理想的な出力と見なされるのかをより良く理解できます。 そして、Claudeがよく構成された出力を返し、 食品の選択肢と量に関する詳細情報を含み、 最も重要なのは、アスリートの目標と制限に 合致することであるという考えを、より強化します。 さて、セルを実行し、 そして評価を再度実行して、どれだけ良くなったか見てみましょう。 これを再実行しますが、上昇するでしょうか、 それとも下降するでしょうか。 少しだけ上昇して7.96になりました。 それではまとめましょう。この技術は ワンショットまたはマルチショットプロンプティングと呼ばれます。 ワンショットは単一の例を提供するもので、 マルチショットは複数の例を提供するものです。 そして、これは、Claudeにコーナーケースを処理させたい場合、 または特にClaudeに 特定の複雑な出力形式に一致させたい場合によく使用する テクニックです。
