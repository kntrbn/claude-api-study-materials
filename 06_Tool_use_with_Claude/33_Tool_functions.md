# 33. Tool functions

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287756
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Tool functions
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building AI applications with Claude, you'll often need to give it access to real-time information or the ability to perform actions. This is where tool functions come in - they're Python functions that Claude can call when it needs additional data to help users.

The image above shows three essential tools we'll be implementing: getting the current date/time, adding duration to dates, and setting reminders. Let's start with the first one.

What Are Tool Functions?

A tool function is a plain Python function that gets executed automatically when Claude decides it needs extra information to help a user. For example, if someone asks "What time is it?", Claude would call your date/time tool to get the current time.

Here's an example of a weather tool function. Notice how it validates inputs and provides clear error messages - these are important best practices.

Best Practices for Tool Functions

When writing tool functions, follow these guidelines:

Use descriptive names: Both your function name and parameter names should clearly indicate their purpose
Validate inputs: Check that required parameters aren't empty or invalid, and raise errors when they are
Provide meaningful error messages: Claude can see error messages and might retry the function call with corrected parameters

The validation is particularly important because Claude learns from errors. If you raise a clear error like "Location cannot be empty", Claude might try calling the function again with a proper location value.

Building Your First Tool Function

Let's create a function to get the current date and time. This function will accept a date format parameter so Claude can request the time in different formats:

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)

This function uses Python's datetime module to get the current time and format it according to the provided format string. The default format gives us year-month-day hour:minute:second.

You can test it with different formats:

# Default format: "2024-01-15 14:30:25"
get_current_datetime()

# Just hour and minute: "14:30"
get_current_datetime("%H:%M")

The validation check ensures Claude can't pass an empty string for the date format. While this specific error is unlikely, it demonstrates the pattern of validating inputs and providing helpful error messages that Claude can learn from.

Next Steps

Creating the function is just the first step. Next, you'll need to write a JSON schema that describes the function to Claude, then integrate it into your chat system. This tool function approach gives Claude powerful capabilities while keeping your code organized and maintainable.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                001_tools.ipynb
                                                (opens in new tab)

---

## 🎬 Transcript (English)

Let's get started working on our first tool, which is going to allow Claude to retrieve the current date time. Before we go any further, I want you to know that I've created a new notebook for you to use. This notebook is titled 001 Tools, and it is attached to this lecture. Inside this notebook, you're going to find a lot of the same code we've already written out inside the course. However, I've also added in a new cell down here, titled Tools and Schemas. Inside this cell, I've placed a tremendous amount of boilerplate code just to save us a little bit of time later on. In particular, you're going to find the add duration to date time function, which you are going to use a little bit later on. So again, I would encourage you to download this notebook that is attached to this lecture and use it as the starting point. All right. So now, once again, we're going to be focused on implementing this first tool of Git the current date time. I'm going to walk you through this entire process step by step. We're going to write out a lot of code inside of our notebook, and we're not going to use any of those helper functions that we've set up inside there. The ones like add user message and add assistant message and so on. The reason for this is that you're going to see that we need to refactor those functions just a little bit to suit tools. So rather than trying to mix updating those helper functions and learn about tools at the same time, that would be really confusing. So we're going to instead just focus on making a tool call without using any helper functions as much as possible. OK, so let's get to it. I've broken down this entire process into several different steps. Step one, whenever we are adding in a tool to our implementation, is to write out a tool function. A tool function is a plain Python function that is going to be executed automatically at some point in time when Claude decides that it needs to retrieve some extra information in order to help the user in some way. I've got an example of a possible tool function on the right-hand side called get weather. Claude might be able to make use of this tool function in order to retrieve the current weather at some particular location in the world. Now there's a couple of best practices around tool functions. First, we always want to use well-named and descriptive arguments. So the actual function itself and the arguments to receive should be reasonably well-named and at least give us a hint of what they are about. Second, we want to validate these inputs and raise an error if anything is wrong with the input itself. So for example, if we failed to receive a location or if the location is an empty string, we would want to raise an error immediately. And then finally, whenever we do raise an error, we want to make sure that it contains some kind of a meaningful error message. In some cases, if Claude tries to call a tool function, and it results in an error, Claude is going to see the exact error message. And Claude might decide to try to call your tool function again and call it in a slightly different way that attempts to correct for that error. So for example, you can imagine if that if Claude tries to call this get weather function, and it passes in an empty string, the validation check at the very top would fail, and we would raise an error. Claude would see the error message of location cannot be empty. And Claude might then decide to try to call this tool function again, making sure that it passes in not an empty string anymore. All right, so let's go back over to our notebook, and we're going to put together our first tool function. Remember, the goal of the tool we are putting together is to get the current date time. So back over here, I'm going to add a new cell at the very bottom and I will define a new function called get current date time. This is going to take in an argument that I will call date format. I will give it a default value. It's going to be a little bit of a complicated string here. I'm going to put in percent capital Y, percent lowercase M, percent lowercase d, and then a space, a percent H colon, percent M colon, percent S. Now that string is a little bit complicated, so I would encourage you to pause the video right here and double check the string you've put in, make sure it exactly matches what I have. Then inside this function, I'm going to use that date format to get the current date time and format it in a way that matches this date format string. So I will return datetime.now.strftime, I'll pass in that date format. So now as a quick example of how we would actually use this function, we could call get current date time. And if we ran it just like this, we would get back a date time in the format of year, month, day, hour, minute, second. Or alternatively, I could put in a custom date format string of something like percent H, colon, percent, capital M. And that will print out just the hour and minute of my current time. A good improvement to this function would be to add in some validation of the date format argument. Unfortunately, we can't very easily validate the exact structure. Make sure that this thing is a valid string format time formatter. But we can at least check and make sure that we are not passing in an empty string. So I might decide to add in a little bit of validation here with a if not date format. And then if we fail that validation check, I might raise a value error and say something like date format cannot be empty. So now if I try to call get current daytime with an empty string, I would end up getting an error message and it's going to tell me date format cannot be empty. Now to be honest with you, it's kind of unlikely that Claude is going to make this mistake of passing in an empty string here, but at least from the off chance that it does, we are providing some signal back to Claude and we are kind of telling it how it can fix up the error. It can try to call get current date time again and make sure that it passes in a date format that is not empty.

---

## 🎬 トランスクリプト（日本語）

最初のツールとして、現在の日時を取得できるようにしましょう。 先に進む前に、新しいノートブックを作成したことをお伝えしておきます。 このノートブックは、あなたが使用するためのものです。ノートブックの名前は「001 ツール」で、この講義に添付されています。 このノートブックの中には、コースで既に作成したコードの多くが含まれています。 しかし、ここにも新しいセルを追加しました。 「ツールとスキーマ」と名付けられています。 このセルには、時間を節約するために 大量の定型コードを配置しました。 後で少し時間を節約するためです。 特に、あなたは「日時への期間の追加」関数を見つけるでしょう。 これは、後で少し使用することになります。 ですので、この講義に添付されているこのノートブックをダウンロードし、 出発点として使用することを強くお勧めします。 さて。 もう一度言いますが、私たちはこの最初のツール、 つまり現在の日時を取得するツールの実装に焦点を当てます。 私はあなたにこの全プロセスをステップバイステップで説明します。 ノートブックの中にたくさんのコードを書き込みますが、 用意したヘルパー関数は使用しません。 「ユーザーメッセージの追加」や「アシスタントメッセージの追加」などの関数です。 これらを使用しない理由は、ツールに合わせて これらの関数を少しリファクタリングする必要があることがわかるからです。 なので、これらのヘルパー関数を更新することとツールについて学ぶことを 同時に行おうとすると、非常に混乱するでしょう。 そのため、代わりにツール呼び出しに焦点を当てます。 ヘルパー関数をできるだけ使用しないようにします。 OK。 では、始めましょう。この全プロセスを いくつかの異なるステップに分けました。ステップ1は、 実装にツールを追加する際は、ツール関数を書くことです。 ツール関数とは、Claudeが ユーザーを助けるために追加情報が必要だと判断したときに 自動的に実行されるプレーンなPython関数です。 右側には、`get_weather` という 可能なツール関数の例があります。 Claude は、このツール関数を利用して 世界のどこかの現在の天気を取得するかもしれません。 ツール関数には、いくつかのベストプラクティスがあります。第一に、 常に分かりやすく説明的な引数を使用することです。 つまり、関数自体と受け取る引数は、 それらが何であるかを示唆するような、 それなりにわかりやすい名前であるべきです。 第二に、これらの入力を検証し、 入力自体に問題がある場合はエラーを発生させる必要があります。 例えば、場所が指定されなかった場合や、 場所が空文字列だった場合は、すぐにエラーを発生させたいでしょう。 そして最後に、エラーを発生させる際は、 意味のあるエラーメッセージが含まれていることを確認する必要があります。 場合によっては、Claudeがツール関数を呼び出して エラーが発生した場合、Claudeは正確なエラーメッセージを見て、 再度ツール関数を呼び出そうとするかもしれません。 そして、エラーを修正しようと、 少し異なる方法で呼び出すかもしれません。 例えば、Claudeがこの`get_weather`関数を呼び出して 空文字列を渡した場合、 先頭の検証チェックが失敗し、エラーが発生します。 Claudeは「場所は空にできません」というエラーメッセージを見て、 再度ツール関数を呼び出すことを決定するかもしれません。 そして、空ではない値を渡すようにします。 さて、ノートブックに戻りましょう。最初のツール関数を作成します。 作成しているツールの目的は、現在の日時を取得することです。 ここに移動して、一番下に新しいセルを追加し、 `get_current_date_time` という新しい関数を定義します。 引数として `date_format` を取ります。 デフォルト値を設定します。少し 複雑な文字列にします。パーセント大文字のY、パーセント小文字のM、 パーセント小文字のd、そしてスペース、 パーセント大文字のH、コロン、パーセント小文字のM、 コロン、パーセント小文字のSを入れます。 この文字列は少し複雑なので、 ここで動画を一時停止して、 入力した文字列をダブルチェックすることをお勧めします。 私が持っているものと正確に一致していることを確認してください。 そして、この関数の中で、その`date_format`を使用して 現在の日時を取得し、その`date_format`文字列に 一致するようにフォーマットします。`datetime.now().strftime`を返します。 `date_format`を渡します。 では、この関数を実際に使用する方法の簡単な例として、 `get_current_date_time()` を呼び出すことができます。 そして、このように実行すると、年、月、日、時、分、秒のフォーマットで 日時が返されます。 または、例えば、パーセント大文字のH、コロン、パーセント小文字のMのような カスタム日付フォーマット文字列を入力することもできます。 そうすると、現在の時刻の時と分だけが表示されます。 この関数を改善するなら、 `date_format` 引数の検証を追加することです。 残念ながら、正確な構造を検証することはできません。 このものが有効な文字列フォーマットタイムフォーマッターであることを確認することはできません。 しかし、少なくとも、空文字列を渡していないことを確認することはできます。 なので、ここに少し検証を追加するかもしれません。 `if not date_format:` で。 そして、その検証チェックに失敗した場合は、 `ValueError` を発生させて、「日付フォーマットは空にできません」と言うかもしれません。 さて、ここで空文字列で `get_current_date_time` を呼び出そうとすると、エラーメッセージが表示され、 「日付フォーマットは空にできません」と表示されます。 正直に言うと、Claudeが空文字列を渡すような間違いをすることは ほとんどありませんが、 少なくとも万が一そのようなことがあった場合、 Claudeにシグナルを送り、 エラーをどのように修正できるかを伝えています。 Claudeは `get_current_date_time` を再度呼び出して、 空でない`date_format`を渡すようにします。 それでは、今度は 空文字列を渡すことなく、このツールを実際に使用する方法を試してみましょう。 つまり、Claudeは例えば それを呼び出して、適切なフォーマットを渡すことを期待しています。 それができなければ、私たちはここでエラーを報告し、 Claudeにそれを修正する方法を教えます。 Claudeは再度呼び出し、 日付フォーマットを空にしないようにします。 さて、これで私たちはそのツール関数を作成したので、 次はそれを実際に使用する方法を見ていきましょう。
