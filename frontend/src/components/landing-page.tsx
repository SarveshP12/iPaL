"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  MessageSquare,
  Sparkles,
  Zap,
  Shield,
  TrendingUp,
  Users,
  ArrowRight,
  CheckCircle2,
  Brain,
  Database,
  Send,
} from "lucide-react"
import { cn } from "@/lib/utils"

export default function LandingPage() {
  const [chatMessage, setChatMessage] = useState("")

  const features = [
    {
      icon: Brain,
      title: "Intelligent Responses",
      description: "Powered by advanced RAG technology for accurate, context-aware answers",
      gradient: "from-blue-500 to-cyan-500",
    },
    {
      icon: Database,
      title: "Knowledge Retrieval",
      description: "Access vast banking knowledge base instantly with semantic search",
      gradient: "from-purple-500 to-pink-500",
    },
    {
      icon: Zap,
      title: "Lightning Fast",
      description: "Get instant responses with optimized query processing",
      gradient: "from-orange-500 to-yellow-500",
    },
    {
      icon: Shield,
      title: "Secure & Compliant",
      description: "Bank-grade security with complete data privacy and compliance",
      gradient: "from-green-500 to-emerald-500",
    },
    {
      icon: Users,
      title: "Personalized Experience",
      description: "Tailored interactions based on user context and preferences",
      gradient: "from-red-500 to-rose-500",
    },
    {
      icon: TrendingUp,
      title: "Continuous Learning",
      description: "Improves over time with machine learning and user feedback",
      gradient: "from-indigo-500 to-blue-500",
    },
  ]

  const stats = [
    { value: "99.9%", label: "Uptime" },
    { value: "< 2s", label: "Response Time" },
    { value: "10M+", label: "Queries Handled" },
    { value: "95%", label: "User Satisfaction" },
  ]

  const steps = [
    {
      number: "01",
      title: "Ask Your Question",
      description: "Type your banking query in natural language - no technical jargon needed",
    },
    {
      number: "02",
      title: "AI Processing",
      description: "Our RAG system retrieves relevant information from the knowledge base",
    },
    {
      number: "03",
      title: "Get Smart Answers",
      description: "Receive accurate, contextual responses tailored to your needs",
    },
  ]

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-50 via-blue-50 to-indigo-50">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        {/* Animated Background */}
        <div className="absolute inset-0 overflow-hidden">
          <div className="absolute -top-40 -right-40 w-80 h-80 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob" />
          <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000" />
          <div className="absolute top-1/2 left-1/2 w-80 h-80 bg-pink-400 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000" />
        </div>

        <div className="relative container mx-auto px-6 py-20 lg:py-32">
          <div className="flex flex-col lg:flex-row items-center justify-between gap-12">
            {/* Left Content */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="flex-1 text-center lg:text-left"
            >
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-blue-100 rounded-full text-blue-600 text-sm font-medium mb-6">
                <Sparkles className="w-4 h-4" />
                <span>Powered by Advanced AI</span>
              </div>

              <h1 className="text-5xl lg:text-7xl font-bold text-slate-900 mb-6 leading-tight">
                Meet <span className="bg-linear-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">iPaL</span>
                <br />
                Your Intelligent Banking Assistant
              </h1>

              <p className="text-xl text-slate-600 mb-8 max-w-2xl">
                Experience the future of banking with our RAG-powered chatbot. Get instant, accurate answers
                to all your banking queries with human-like understanding.
              </p>

              <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                <button className="group px-8 py-4 bg-linear-to-r from-blue-600 to-purple-600 text-white rounded-xl font-semibold hover:shadow-lg hover:scale-105 transition-all duration-200 flex items-center justify-center gap-2">
                  Start Chatting
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </button>
                <button className="px-8 py-4 bg-white text-slate-900 rounded-xl font-semibold border-2 border-slate-200 hover:border-blue-600 hover:shadow-lg transition-all duration-200">
                  Watch Demo
                </button>
              </div>

              <div className="flex items-center gap-8 mt-12 justify-center lg:justify-start">
                <div className="flex -space-x-3">
                  {[1, 2, 3, 4].map((i) => (
                    <div
                      key={i}
                      className="w-10 h-10 rounded-full bg-linear-to-br from-blue-400 to-purple-600 border-2 border-white"
                    />
                  ))}
                </div>
                <div className="text-left">
                  <p className="text-slate-900 font-semibold">10,000+ Active Users</p>
                  <p className="text-slate-600 text-sm">Trusted by ICICI customers</p>
                </div>
              </div>
            </motion.div>

            {/* Right Content - Chat Demo */}
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="flex-1 w-full max-w-xl"
            >
              <div className="bg-white rounded-2xl shadow-2xl border border-slate-200 overflow-hidden">
                {/* Chat Header */}
                <div className="bg-linear-to-r from-blue-600 to-purple-600 px-6 py-4 flex items-center gap-3">
                  <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />
                  <span className="text-white font-semibold">iPaL Assistant</span>
                </div>

                {/* Chat Messages */}
                <div className="p-6 space-y-4 h-96 overflow-y-auto">
                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="flex gap-3"
                  >
                    <div className="w-8 h-8 rounded-full bg-linear-to-br from-blue-600 to-purple-600 flex items-center justify-center shrink-0">
                      <MessageSquare className="w-4 h-4 text-white" />
                    </div>
                    <div className="bg-linear-to-br from-blue-50 to-purple-50 rounded-2xl rounded-tl-none px-4 py-3 max-w-[80%]">
                      <p className="text-slate-800">
                        Hi! I&apos;m iPaL, your intelligent banking assistant. How can I help you today?
                      </p>
                    </div>
                  </motion.div>

                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3 }}
                    className="flex gap-3 justify-end"
                  >
                    <div className="bg-slate-100 rounded-2xl rounded-tr-none px-4 py-3 max-w-[80%]">
                      <p className="text-slate-800">What are my recent transactions?</p>
                    </div>
                  </motion.div>

                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.6 }}
                    className="flex gap-3"
                  >
                    <div className="w-8 h-8 rounded-full bg-linear-to-br from-blue-600 to-purple-600 flex items-center justify-center shrink-0">
                      <MessageSquare className="w-4 h-4 text-white" />
                    </div>
                    <div className="bg-linear-to-br from-blue-50 to-purple-50 rounded-2xl rounded-tl-none px-4 py-3 max-w-[80%]">
                      <p className="text-slate-800">
                        Here are your recent transactions:
                      </p>
                      <div className="mt-3 space-y-2">
                        {["Amazon - ₹2,499", "Zomato - ₹847", "Electricity Bill - ₹1,234"].map((tx, i) => (
                          <div key={i} className="bg-white rounded-lg px-3 py-2 text-sm text-slate-700">
                            {tx}
                          </div>
                        ))}
                      </div>
                    </div>
                  </motion.div>
                </div>

                {/* Chat Input */}
                <div className="p-4 border-t border-slate-200 bg-slate-50">
                  <div className="flex gap-2">
                    <input
                      type="text"
                      value={chatMessage}
                      onChange={(e) => setChatMessage(e.target.value)}
                      placeholder="Ask me anything..."
                      className="flex-1 px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
                    />
                    <button className="px-6 py-3 bg-linear-to-r from-blue-600 to-purple-600 text-white rounded-xl hover:shadow-lg transition-all duration-200">
                      <Send className="w-5 h-5" />
                    </button>
                  </div>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="text-center"
              >
                <div className="text-4xl lg:text-5xl font-bold bg-linear-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2">
                  {stat.value}
                </div>
                <div className="text-slate-600 font-medium">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-linear-to-br from-slate-50 to-white">
        <div className="container mx-auto px-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
              Powerful Features for Smart Banking
            </h2>
            <p className="text-xl text-slate-600 max-w-2xl mx-auto">
              Discover how iPaL transforms your banking experience with cutting-edge AI technology
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="group relative bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 border border-slate-200 hover:border-transparent overflow-hidden"
              >
                <div className={cn(
                  "absolute inset-0 bg-linear-to-br opacity-0 group-hover:opacity-5 transition-opacity duration-300",
                  feature.gradient
                )} />
                
                <div className={cn(
                  "w-14 h-14 rounded-xl bg-linear-to-br flex items-center justify-center mb-6",
                  feature.gradient
                )}>
                  <feature.icon className="w-7 h-7 text-white" />
                </div>

                <h3 className="text-xl font-bold text-slate-900 mb-3">{feature.title}</h3>
                <p className="text-slate-600 leading-relaxed">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
              How iPaL Works
            </h2>
            <p className="text-xl text-slate-600 max-w-2xl mx-auto">
              Simple, fast, and intelligent - banking made easy in three steps
            </p>
          </motion.div>

          <div className="max-w-4xl mx-auto">
            {steps.map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.2 }}
                className="relative flex gap-8 mb-12 last:mb-0"
              >
                {/* Connector Line */}
                {index < steps.length - 1 && (
                  <div className="absolute left-8 top-20 w-0.5 h-full bg-linear-to-b from-blue-600 to-purple-600 opacity-20" />
                )}

                {/* Number Badge */}
                <div className="relative shrink-0">
                  <div className="w-16 h-16 rounded-full bg-linear-to-br from-blue-600 to-purple-600 flex items-center justify-center text-white font-bold text-xl shadow-lg">
                    {step.number}
                  </div>
                </div>

                {/* Content */}
                <div className="flex-1 bg-slate-50 rounded-xl p-6 hover:shadow-lg transition-shadow duration-300">
                  <h3 className="text-2xl font-bold text-slate-900 mb-3">{step.title}</h3>
                  <p className="text-slate-600 leading-relaxed">{step.description}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-linear-to-br from-blue-600 via-purple-600 to-indigo-600 relative overflow-hidden">
        <div className="absolute inset-0 bg-grid-white/[0.05] bg-size-\[20px_20px\]" />
        
        <div className="container mx-auto px-6 relative">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center max-w-3xl mx-auto"
          >
            <h2 className="text-4xl lg:text-5xl font-bold text-white mb-6">
              Ready to Transform Your Banking Experience?
            </h2>
            <p className="text-xl text-blue-100 mb-8">
              Join thousands of satisfied customers using iPaL for smarter, faster banking
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <button className="group px-8 py-4 bg-white text-blue-600 rounded-xl font-semibold hover:shadow-2xl hover:scale-105 transition-all duration-200 flex items-center gap-2">
                Get Started Now
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </button>
              <button className="px-8 py-4 bg-transparent text-white rounded-xl font-semibold border-2 border-white hover:bg-white hover:text-blue-600 transition-all duration-200">
                Contact Sales
              </button>
            </div>

            <div className="flex items-center justify-center gap-6 mt-12 text-white">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5" />
                <span>No credit card required</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5" />
                <span>Free trial available</span>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-slate-300 py-12">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="mb-4 md:mb-0">
              <h3 className="text-2xl font-bold text-white mb-2">iPaL</h3>
              <p className="text-slate-400">Intelligent Personal Assistant Layer</p>
            </div>
            <div className="text-center md:text-right">
              <p className="text-slate-400">© 2026 ICICI Bank. All rights reserved.</p>
              <p className="text-sm text-slate-500 mt-1">Powered by Advanced RAG Technology</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
