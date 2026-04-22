"use client"

import { useRef } from "react"
import { useFrame } from "@react-three/fiber"
import { Mesh } from "three"

export default function AIChip() {
  const chipRef = useRef<Mesh>(null)
  const glowRef = useRef<Mesh>(null)

  useFrame((state) => {
    if (chipRef.current) {
      chipRef.current.rotation.y = state.clock.elapsedTime * 0.3
      chipRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.5) * 0.1
    }
    if (glowRef.current) {
      glowRef.current.scale.setScalar(1 + Math.sin(state.clock.elapsedTime * 2) * 0.05)
    }
  })

  return (
    <group>
      {/* Main Chip Body */}
      <mesh ref={chipRef}>
        <boxGeometry args={[2, 2, 0.3]} />
        <meshStandardMaterial
          color="#0a0a0a"
          metalness={0.9}
          roughness={0.1}
          emissive="#10b981"
          emissiveIntensity={0.2}
        />
      </mesh>

      {/* Center Glow */}
      <mesh ref={glowRef} position={[0, 0, 0.2]}>
        <boxGeometry args={[1.2, 1.2, 0.1]} />
        <meshStandardMaterial
          color="#10b981"
          emissive="#10b981"
          emissiveIntensity={2}
          transparent
          opacity={0.8}
        />
      </mesh>

      {/* Chip Pins */}
      {[...Array(8)].map((_, i) => {
        const angle = (i / 8) * Math.PI * 2
        const x = Math.cos(angle) * 1.3
        const y = Math.sin(angle) * 1.3
        return (
          <mesh key={i} position={[x, y, -0.15]}>
            <boxGeometry args={[0.15, 0.15, 0.3]} />
            <meshStandardMaterial
              color="#10b981"
              metalness={0.8}
              roughness={0.2}
              emissive="#10b981"
              emissiveIntensity={0.5}
            />
          </mesh>
        )
      })}

      {/* Circuit Lines */}
      {[...Array(4)].map((_, i) => {
        const rotation = (i / 4) * Math.PI * 2
        return (
          <group key={`line-${i}`} rotation={[0, 0, rotation]}>
            <mesh position={[0.8, 0, 0.16]}>
              <boxGeometry args={[0.6, 0.05, 0.02]} />
              <meshStandardMaterial
                color="#10b981"
                emissive="#10b981"
                emissiveIntensity={1}
              />
            </mesh>
          </group>
        )
      })}

      {/* Ambient Light for the chip */}
      <pointLight position={[0, 0, 2]} intensity={1} color="#10b981" />
    </group>
  )
}
