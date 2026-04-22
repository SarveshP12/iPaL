"use client"

import { useState, Suspense } from "react"
import { Canvas } from "@react-three/fiber"
import { OrbitControls, PerspectiveCamera } from "@react-three/drei"
import { motion } from "framer-motion"
import {
  MessageSquare,
  Sparkles,
  Shield,
  Zap,
  ChevronDown,
  Menu,
  X,
  ArrowRight,
} from "lucide-react"
import AIChip from "./ai-chip"
import AnimatedWaves from "./animated-waves"

export default function LandingPage() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const features = [
    {
      icon: MessageSquare,
      title: "Conversational AI",
      description: "Natural language understanding for seamless banking interactions",
    },
    {
      icon: Shield,
      title: "Bank-Grade Security",
      description: "Enterprise-level encryption and data protection",
    },
    {
      icon: Zap,
      title: "Lightning Fast",
      description: "Sub-second response times for all queries",
    },
  ]

  return (
    <div className="min-h-screen bg-black text-white relative overflow-hidden">
      <AnimatedWaves />

      {/* Navigation - floating pill */}
      <nav className="fixed top-6 left-0 right-0 z-50 flex justify-center pointer-events-none">
        <div className="pointer-events-auto flex items-center justify-between w-full max-w-5xl rounded-full border border-emerald-500/30 bg-black/70 px-6 py-3 shadow-lg backdrop-blur-xl">
          {/* Logo */}
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              className="flex items-center gap-2 group cursor-pointer"
            >
              <div className="relative">
                <div className="w-10 h-10 bg-emerald-500 rounded-lg flex items-center justify-center group-hover:animate-glow transition-all duration-300">
                  <Sparkles className="w-6 h-6 text-black" />
                </div>
              </div>
              <span className="text-2xl font-bold bg-linear-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
                iPaL
              </span>
            </motion.div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center gap-8">
              {["Overview", "Technology", "Testimonials", "Resources"].map((item, index) => (
                <motion.button
                  key={item}
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="text-gray-300 hover:text-emerald-400 transition-all duration-300 relative group"
                >
                  {item}
                  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-emerald-400 group-hover:w-full transition-all duration-300" />
                </motion.button>
              ))}
          </div>

          {/* CTA Buttons */}
          <div className="hidden md:flex items-center gap-4">
              <motion.button
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                className="text-gray-300 hover:text-white transition-all duration-300 px-6 py-2 rounded-lg hover:bg-white/5"
              >
                Log In
              </motion.button>
              <motion.button
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.1 }}
                className="bg-emerald-500 text-black px-6 py-2 rounded-lg font-semibold hover:bg-emerald-400 transition-all duration-300 hover:shadow-[0_0_30px_rgba(16,185,129,0.5)] hover:scale-105"
              >
                Get Started
              </motion.button>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="md:hidden text-white"
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="pointer-events-auto md:hidden mt-3 space-y-3 max-w-5xl w-full px-6"
          >
            {["Overview", "Technology", "Testimonials", "Resources"].map((item) => (
              <button
                key={item}
                className="block w-full text-left text-gray-300 hover:text-emerald-400 transition-colors py-2"
              >
                {item}
              </button>
            ))}
            <button className="w-full text-left text-gray-300 hover:text-white transition-colors py-2">
              Log In
            </button>
            <button className="w-full bg-emerald-500 text-black px-6 py-2 rounded-lg font-semibold hover:bg-emerald-400 transition-all duration-300">
              Get Started
            </button>
          </motion.div>
        )}
      </nav>

      {/* Hero Section */}
      <section className="relative z-10 container mx-auto px-6 pt-40 pb-24">
        <div className="flex flex-col items-center text-center">
          {/* 3D Model */}
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1 }}
            className="w-full max-w-md h-100 mb-6 animate-float"
          >
            <Suspense fallback={<div className="w-full h-full flex items-center justify-center">
              <div className="w-16 h-16 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin" />
            </div>}>
              <Canvas>
                <PerspectiveCamera makeDefault position={[0, 0, 6]} />
                <ambientLight intensity={0.5} />
                <directionalLight position={[10, 10, 5]} intensity={1} />
                <AIChip />
                <OrbitControls enableZoom={false} enablePan={false} />
              </Canvas>
            </Suspense>
          </motion.div>

          {/* Hero Text */}
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="text-5xl md:text-7xl lg:text-8xl font-bold mb-6 leading-tight"
          >
            <span className="bg-linear-to-r from-white via-emerald-200 to-white bg-clip-text text-transparent">
              Verify to Trust AI
            </span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="text-xl md:text-2xl text-gray-400 mb-8 max-w-3xl"
          >
            Introducing Verifiable Compute. Ready for
            <br />
            the Agentic AI Era.
          </motion.p>

          {/* CTA Button */}
          <motion.button
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.7 }}
            className="group flex items-center gap-3 bg-emerald-500 text-black px-8 py-4 rounded-full font-semibold text-lg hover:bg-emerald-400 transition-all duration-300 hover:shadow-[0_0_40px_rgba(16,185,129,0.6)] hover:scale-105"
          >
            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            Schedule Demo
          </motion.button>

          {/* Scroll Indicator */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1, duration: 1 }}
            className="mt-20"
          >
            <ChevronDown className="w-8 h-8 text-emerald-400 animate-bounce" />
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="relative z-10 container mx-auto px-6 py-20">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-5xl font-bold mb-4">
            Preorders Q4 Ship <span className="text-emerald-400">2025</span>
          </h2>
        </motion.div>

        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.2 }}
              whileHover={{ y: -10, transition: { duration: 0.3 } }}
              className="group relative bg-linear-to-b from-emerald-500/10 to-transparent border border-emerald-500/20 rounded-2xl p-8 backdrop-blur-sm hover:border-emerald-500/50 transition-all duration-300 cursor-pointer"
            >
              {/* Icon */}
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-emerald-500/20 blur-2xl rounded-full group-hover:bg-emerald-500/40 transition-all duration-300" />
                <div className="relative w-16 h-16 bg-linear-to-br from-emerald-500 to-teal-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                  <feature.icon className="w-8 h-8 text-black" />
                </div>
              </div>

              {/* Content */}
              <h3 className="text-xl font-bold mb-3 text-white group-hover:text-emerald-400 transition-colors duration-300">
                {feature.title}
              </h3>
              <p className="text-gray-400 leading-relaxed">{feature.description}</p>

              {/* Hover Arrow */}
              <div className="absolute bottom-8 right-8 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <ArrowRight className="w-6 h-6 text-emerald-400 group-hover:translate-x-2 transition-transform" />
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Stats Section */}
      <section className="relative z-10 container mx-auto px-6 py-20">
        <div className="max-w-5xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8">
            {[
              { value: "99.9%", label: "Uptime SLA" },
              { value: "<100ms", label: "Response Time" },
              { value: "10M+", label: "Queries/Day" },
              { value: "256-bit", label: "Encryption" },
            ].map((stat, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.8 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="text-center group cursor-pointer"
              >
                <div className="text-5xl font-bold mb-2 bg-linear-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent group-hover:scale-110 transition-transform duration-300">
                  {stat.value}
                </div>
                <div className="text-gray-400 group-hover:text-emerald-400 transition-colors duration-300">
                  {stat.label}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative z-10 container mx-auto px-6 py-32">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="max-w-4xl mx-auto text-center"
        >
          <div className="relative">
            <div className="absolute inset-0 bg-emerald-500/20 blur-3xl rounded-full" />
            <div className="relative bg-linear-to-br from-emerald-500/10 to-transparent border border-emerald-500/30 rounded-3xl p-12 backdrop-blur-sm">
              <h2 className="text-4xl md:text-6xl font-bold mb-6">
                Ready to Experience the Future?
              </h2>
              <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
                Join the waitlist and be among the first to access iPaL&apos;s revolutionary AI banking assistant
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <button className="group bg-emerald-500 text-black px-8 py-4 rounded-full font-semibold text-lg hover:bg-emerald-400 transition-all duration-300 hover:shadow-[0_0_40px_rgba(16,185,129,0.6)] hover:scale-105 flex items-center justify-center gap-2">
                  Get Early Access
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </button>
                <button className="px-8 py-4 rounded-full font-semibold text-lg border-2 border-emerald-500 text-emerald-400 hover:bg-emerald-500/10 transition-all duration-300">
                  Learn More
                </button>
              </div>
            </div>
          </div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="relative z-10 border-t border-emerald-500/10 py-8">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center">
                <Sparkles className="w-5 h-5 text-black" />
              </div>
              <span className="text-xl font-bold">iPaL</span>
            </div>
            <div className="text-gray-400 text-sm">
              © 2026 ICICI Bank. Powered by Advanced RAG Technology.
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
