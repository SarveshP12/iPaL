"use client"

export default function AnimatedWaves() {
  return (
    <div className="absolute inset-0 overflow-hidden opacity-30">
      {/* Wave 1 */}
      <svg
        className="absolute w-full h-full animate-wave-slow"
        style={{ top: "10%" }}
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="none"
          stroke="url(#gradient1)"
          strokeWidth="2"
          d="M0,160 C320,100 420,220 720,160 C1020,100 1120,220 1440,160 L1440,0 L0,0 Z"
        />
        <defs>
          <linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#14b8a6" stopOpacity="0.5" />
            <stop offset="50%" stopColor="#10b981" stopOpacity="1" />
            <stop offset="100%" stopColor="#14b8a6" stopOpacity="0.5" />
          </linearGradient>
        </defs>
      </svg>

      {/* Wave 2 */}
      <svg
        className="absolute w-full h-full animate-wave-medium"
        style={{ top: "40%" }}
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="none"
          stroke="url(#gradient2)"
          strokeWidth="2"
          d="M0,100 C360,160 540,40 900,100 C1260,160 1440,40 1440,100 L1440,0 L0,0 Z"
        />
        <defs>
          <linearGradient id="gradient2" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#0d9488" stopOpacity="0.5" />
            <stop offset="50%" stopColor="#14b8a6" stopOpacity="1" />
            <stop offset="100%" stopColor="#0d9488" stopOpacity="0.5" />
          </linearGradient>
        </defs>
      </svg>

      {/* Wave 3 */}
      <svg
        className="absolute w-full h-full animate-wave-fast"
        style={{ bottom: "10%" }}
        viewBox="0 0 1440 320"
        preserveAspectRatio="none"
      >
        <path
          fill="none"
          stroke="url(#gradient3)"
          strokeWidth="2"
          d="M0,220 C400,280 640,160 1000,220 C1200,260 1320,200 1440,220 L1440,0 L0,0 Z"
        />
        <defs>
          <linearGradient id="gradient3" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#10b981" stopOpacity="0.5" />
            <stop offset="50%" stopColor="#14b8a6" stopOpacity="1" />
            <stop offset="100%" stopColor="#10b981" stopOpacity="0.5" />
          </linearGradient>
        </defs>
      </svg>

      {/* Grid overlay */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(16,185,129,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(16,185,129,0.03)_1px,transparent_1px)] bg-size-[50px_50px]" />
    </div>
  )
}
